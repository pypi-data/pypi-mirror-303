from raft.tasks import task
from .base import AzureTask
from ..base.utils import dump_yaml
from ..base.utils import notice, notice_end


@task(klass=AzureTask)
def whoami(ctx, creds=None, **kwargs):
    """
    calls the whoami endpoint in the graph api
    """
    from affliction.graph_client import SynchronousGraphClient
    notice('calling whoami')
    tenant_id = kwargs.get('tenant_id')
    api = SynchronousGraphClient(tenant_id=tenant_id, creds=creds)
    result = api.whoami()
    notice_end()
    dump_yaml(result, quiet=False)
