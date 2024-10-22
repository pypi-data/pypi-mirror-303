import logging
import copy
import json

import torch
import torch.multiprocessing as mp
import torch.distributed as dist

from icflow.utils.runtime import RuntimeContext

logger = logging.getLogger(__name__)


class TorchRuntimeContext(RuntimeContext):
    """
    This holds runtime information for the session, which is mostly
    useful in a distributed setting.
    """

    def __init__(
        self,
        node_id: int = 0,
        num_nodes: int = 1,
        gpus_per_node: int = 1,
        local_rank: int = 0,
    ) -> None:

        super().__init__(node_id, num_nodes, gpus_per_node, local_rank)

        self.dist_backend = "nccl"

    def serialize(self):

        base_serialized = super().serialize()
        base_serialized["dist_backend"] = self.dist_backend
        return base_serialized

    def __str__(self):
        return json.dumps(self.serialize())

    def init(self) -> None:
        """
        If we're running in a multigpu context set up the process group
        """

        if self.is_initialized:
            return

        super().init()

        if not self.is_multigpu:
            return

        logger.info("Starting torch dist process group")
        logging.info("Network info: %s", self.network_context)
        dist.init_process_group(
            backend=self.dist_backend, world_size=self.world_size, rank=self.global_rank
        )

    def sync_dict(self, input_dict: dict) -> dict:
        """
        If we are running in on multiple gpus sync dict across devices
        """

        if not self.is_multigpu:
            return input_dict

        dict_copy = copy.deepcopy(input_dict)
        dist.barrier()

        for outer_key, outer_value in dict_copy.items():
            for key, value in outer_value.items():
                value_tensor = torch.tensor(value, device=self.device.handle)
                dist.all_reduce(value_tensor, op=dist.ReduceOp.AVG)
                input_dict[outer_key][key] = value_tensor
        return input_dict

    def log_cuda_info(self):
        if torch.cuda.is_available():
            num_cuda_devices = torch.cuda.device_count()

            logger.info("Supported cuda arch: %s", torch.cuda.get_arch_list())
            logger.info("Num cuda devices: %d", num_cuda_devices)
            for idx in range(num_cuda_devices):

                device_name = torch.cuda.get_device_name(idx)
                logger.info("Querying device: %d", idx)
                logger.info("Name: %s", device_name)

                device_props = torch.cuda.get_device_properties(idx)
                logger.info("Propeties: %s", device_props)

                memory_use = torch.cuda.memory_usage(idx)
                logger.info("Memory use: %s", memory_use)

                processor_use = torch.cuda.utilization(idx)
                logger.info("Processor use: %s", processor_use)

            if num_cuda_devices > 1:
                logger.info(
                    "p2p access available: %s", torch.cuda.can_device_access_peer(0, 1)
                )
        else:
            logger.info("Cuda not available on system")

    def log_torch_dist_info(self):
        if dist.is_available():
            logger.info("Torch dist is available")

            if dist.is_nccl_available():
                logger.info("Has NCCL")
                nccl_version = torch.cuda.nccl.version()
                logger.info("Nccl version: %s", nccl_version)
            else:
                logger.info("NCCL Backend not found")

            if dist.is_gloo_available():
                logger.info("Has Gloo")
            else:
                logger.info("Gloo Backend not found")

            if dist.is_mpi_available():
                logger.info("Has MPI")
            else:
                logger.info("MPI Backend not found")
        else:
            logger.info("Torch dist not available")

    def log_system_info(self):

        super().log_system_info()

        logger.info("PyTorch Version: %s", torch.__version__)

        self.log_cuda_info()

        self.log_torch_dist_info()

    def per_device_func(self, rank, world_size):
        logger.info("Hello from rank: %d of %d", rank, world_size)

        dist.init_process_group(self.dist_backend, rank=rank, world_size=world_size)

        logger.info("Dist initialized ok: %s", dist.is_initialized())
        logger.info("Running on backend: %s", dist.get_backend())
        logger.info("Torch Dist Rank: %d", dist.get_rank())
        logger.info("Torch Dist World Size: %d", dist.get_world_size())
        logger.info("Current cuda device: %s", torch.cuda.current_device())

        output = torch.tensor([rank]).cuda(rank)
        logger.info("Current tensor: %s", output)
        s = torch.cuda.Stream()

        _ = dist.all_reduce(output, async_op=True)
        with torch.cuda.stream(s):
            s.wait_stream(torch.cuda.default_stream())
            output.add_(100)
        if rank == 0:
            logger.info("Updated tensor: %s", output)

        self.test_p2p()

    def launch_per_device(self):
        mp.spawn(
            self.per_device_func,
            args=(self.world_size,),
            nprocs=self.world_size,
            join=True,
        )

    def test_p2p(self):
        rank = dist.get_rank()
        if rank == 0:
            to_send = torch.tensor([3]).cuda(rank)
            logger.info("Sending to 1")
            dist.send(to_send, 1)
        elif rank == 1:
            to_recv = torch.tensor([0]).cuda(rank)
            sender_rank = dist.recv(to_recv, 0)  # no recv any source on nccl
            logger.info("Recv'd %s from % d", to_recv, sender_rank)
