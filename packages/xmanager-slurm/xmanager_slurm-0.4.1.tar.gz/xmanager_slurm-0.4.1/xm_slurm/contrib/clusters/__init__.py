import datetime as dt
import logging
import os

from xmanager import xm

from xm_slurm import config, resources
from xm_slurm.contrib.clusters import drac
from xm_slurm.executors import Slurm

# ComputeCanada alias
cc = drac

__all__ = ["drac", "mila", "cc"]

logger = logging.getLogger(__name__)


def mila(
    *,
    user: str | None = None,
    partition: str | None = None,
    mounts: dict[os.PathLike[str] | str, os.PathLike[str] | str] | None = None,
) -> config.SlurmClusterConfig:
    """Mila Cluster (https://docs.mila.quebec/)."""
    if mounts is None:
        mounts = {
            "/network/scratch/${USER:0:1}/$USER": "/scratch",
            # TODO: move these somewhere common to all cluster configs.
            "/home/mila/${USER:0:1}/$USER/.local/state/xm-slurm": "/xm-slurm-state",
            "/home/mila/${USER:0:1}/$USER/.ssh": "/home/mila/${USER:0:1}/$USER/.ssh",
        }

    def validate(job: xm.Job) -> None:
        assert isinstance(job.executor, Slurm)

        wants_requeue_with_grace_period = (
            job.executor.requeue and job.executor.timeout_signal_grace_period > dt.timedelta(0)
        )
        partition = job.executor.partition or "main"

        if wants_requeue_with_grace_period and (
            partition is None or not partition.endswith("-grace")
        ):
            logger.warning(
                f"Job {job.name} wants requeue with grace period, but partition `{partition}` does not end with '-grace'. "
                "Mila Cluster requires you specify a grace partition. "
                "This may result in the job not being requeued properly."
            )

    return config.SlurmClusterConfig(
        name="mila",
        ssh=config.SlurmSSHConfig(
            user=user,
            host="login.server.mila.quebec",
            host_public_key=config.PublicKey(
                "ssh-ed25519",
                "AAAAC3NzaC1lZDI1NTE5AAAAIBTPCzWRkwYDr/cFb4d2uR6rFlUtqfH3MoLMXPpJHK0n",
            ),
            port=2222,
        ),
        runtime=config.ContainerRuntime.SINGULARITY,
        partition=partition,
        prolog="module load singularity",
        environment={
            "SINGULARITY_CACHEDIR": "$SCRATCH/.apptainer",
            "SINGULARITY_TMPDIR": "$SLURM_TMPDIR",
            "SINGULARITY_LOCALCACHEDIR": "$SLURM_TMPDIR",
            "SCRATCH": "/scratch",
            # TODO: move this somewhere common to all cluster configs.
            "XM_SLURM_STATE_DIR": "/xm-slurm-state",
        },
        mounts=mounts,
        resources={
            resources.ResourceType.RTX8000: "rtx8000",
            resources.ResourceType.V100: "v100",
            resources.ResourceType.A100: "a100",
            resources.ResourceType.A100_80GIB: "a100l",
            resources.ResourceType.A6000: "a6000",
        },
        features={
            resources.FeatureType.NVIDIA_MIG: "mig",
            resources.FeatureType.NVIDIA_NVLINK: "nvlink",
        },
        validate=validate,
    )
