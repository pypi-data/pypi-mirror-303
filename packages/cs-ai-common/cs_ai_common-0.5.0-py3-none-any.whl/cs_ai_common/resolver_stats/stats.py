from cs_ai_common.dynamodb.resolver_task_table import update_resolver_task
from cs_ai_common.dynamodb.task_table import update_task
from cs_ai_common.models.resolvers import ResolverStatsModel, TaskStatisticsModel


def save_task_statistics(task_id: str, stats: TaskStatisticsModel) -> None:
    update_task(task_id, Stats=stats.dict())


def save_resolver_statistics(task_id: str, stats: ResolverStatsModel) -> None:
    update_resolver_task(task_id, stats.ResolverName, found=stats.TotalAds)