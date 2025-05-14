import logging
from textwrap import dedent

from dagger import dag, function, object_type
from rich.logging import RichHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(RichHandler())


@object_type
class TestAgent:
    @function
    async def test_agent(self) -> str:
        dockerfile = """
FROM ubuntu:jammy
RUN echo1 "Hello, world!"
"""
        env = (
            dag.env()
            .with_workspace_input(
                'before',
                dag.workspace().write_file('Dockerfile', dockerfile),
                'workspace with tools to complete assignment',
            )
            .with_workspace_output('after', 'workspace with completed assignment')
        )
        llm = (
            dag.llm(max_api_calls=100)
            .with_env(env)
            .with_prompt(
                dedent("""
            You're a senior developer. You have an access to a workspace.
            There is a Dockerfile in the workspace by the path Dockerfile.
            Your task is to fix the Dockerfile and write it to workspace.
            For that task you can build the Dockerfile and check the result.
            Return the workspace with the fixed Dockerfile.
            Don't stop until the Dockerfile is valid.
            """)
            )
        )
        result = llm.env().output('after').as_workspace().container()
        return await result.file('Dockerfile').contents()
