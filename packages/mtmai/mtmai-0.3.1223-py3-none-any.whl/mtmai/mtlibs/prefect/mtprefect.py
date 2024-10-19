import threading

from mtmai.core.logging import get_logger
from mtmai.flows.site_flows import flow_site_automation

logger = get_logger()


def get_prefect_deployments():
    """
    获取所有需要部署的工作流
    """
    #
    # from prefect.automations import Automation
    from prefect.events import DeploymentEventTrigger

    # from prefect.events.actions import CancelFlowRun
    # from prefect.events.schemas.automations import EventTrigger
    # from mtmai.flows.hello_flow import flow_hello
    from mtmai.flows.site_flows import (
        create_site_flow,
        flow_run_gen_article,
        flow_run_task,
    )

    # example
    # automation = Automation(
    #     name="woodchonk",
    #     trigger=EventTrigger(
    #         expect={"animal.walked"},
    #         match={
    #             "genus": "Marmota",
    #             "species": "monax",
    #         },
    #         posture="Reactive",
    #         threshold=3,
    #     ),
    #     actions=[CancelFlowRun()],
    # ).create()

    return [
        # flow_article_gen.to_deployment(name="deployment_article_gen"),
        create_site_flow.to_deployment(
            name="deployment_site_flow",
            triggers=[
                DeploymentEventTrigger(
                    enabled=True,
                    # expect=["mtmai.site.create"],
                    match={"prefect.resource.id": "my.external.resource"},
                    parameters={
                        "user_id": "{{event.resource.user_id}}",
                        "site_id": "{{event.resource.site_id}}",
                    },
                )
            ],
        ),
        # flow_hello.to_deployment(name="deployment_flow_hello"),
        flow_run_gen_article.to_deployment(
            name="deployment_flow_site_gen",
            description="单个站点自动化，将所有全托管的站点进行文章生成",
        ),
        flow_site_automation.to_deployment(
            name="flow_site_automation",
            description="全部站点自动化",
            # interval=60,  # 秒
        ),
        flow_run_task.to_deployment(
            name="flow_run_task",
            description="运行单个mttask任务",
        ),
        # flow_hello_2.to_deployment(
        #     name="flow_hello_2",
        #     triggers=[
        #         DeploymentEventTrigger(
        #             enabled=True,
        #             match={"prefect.resource.id": "my.external.resource"},
        #             # expect=["external.resource.pinged"],
        #             parameters={
        #                 "param_1": "{{ event }}",
        #             },
        #         )
        #     ],
        # ),
    ]


def start_prefect_deployment(asThreading: bool = False):
    """
    部署工作流到 prefect server
    """
    from prefect.variables import Variable

    def start_worker():
        from prefect import serve

        # 设置变量(仅作为练习)
        Variable.set("crew_members", ["Zaphod", "Arthur", "Trillian"], overwrite=True)

        all_deployments = get_prefect_deployments()
        # logger.info(f"启动 prefect 服务, 部署数量: {len(all_deployments)}")
        serve(
            *all_deployments,
            limit=50,  # 默认值5
        )

    if asThreading:
        threading.Thread(target=start_worker).start()
    else:
        start_worker()
