import logging

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
        ws = dag.workspace()
        llm = (
            dag.llm(model='claude-3-5-sonnet-latest', max_api_calls=100)
            .with_workspace(ws.write_file('Dockerfile', dockerfile))
            .with_prompt("""
You're a senior developer. You have an access to a workspace.
There is a Dockerfile in the workspace by the path Dockerfile.
Your task is to fix the Dockerfile and write it to Dockerfile.
For that task you can build the Dockerfile and check the result.
Don't stop until the Dockerfile is valid.
""")
        )
        llm = await llm.sync()
        result = llm.workspace().container()
        return await result.file('Dockerfile').contents()
