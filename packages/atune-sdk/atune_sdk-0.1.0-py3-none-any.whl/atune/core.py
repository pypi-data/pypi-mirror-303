from typing import Dict, Any, Optional, List
import aiohttp
import asyncio
from .exceptions import AtuneError
from .visualization import start_visualization_server

class Atune:
    """
    Main Atune class for monitoring and evaluating LLM applications
    """
    def __init__(
        self,
        api_key: str,
        api_url: Optional[str] = None,
        workflow_id: Optional[str] = None
    ):
        self.api_key = api_key
        self.api_url = api_url or "http://localhost:8000"
        self.workflow_id = workflow_id
        self._setup_client()

    def _setup_client(self):
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def audit(
        self,
        input_content: Any,
        output_content: Any,
        workflow_id: Optional[str] = None,
        **options
    ) -> Dict[str, Any]:
        """
        Audit an LLM execution for safety and quality
        """
        _workflow_id = workflow_id or self.workflow_id
        if not _workflow_id:
            raise AtuneError("workflow_id must be provided")

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.api_url}/api/audit",
                json={
                    "workflow_id": _workflow_id,
                    "input": input_content,
                    "output": output_content,
                    "options": options
                },
                headers=self.headers
            ) as response:
                if response.status != 200:
                    raise AtuneError(f"Audit request failed: {await response.text()}")
                return await response.json()

    async def backtest(
        self,
        prompt_template: str,
        test_cases: List[Dict[str, Any]],
        workflow_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Backtest a prompt template against test cases
        """
        _workflow_id = workflow_id or self.workflow_id
        if not _workflow_id:
            raise AtuneError("workflow_id must be provided")

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.api_url}/api/backtest",
                json={
                    "workflow_id": _workflow_id,
                    "prompt_template": prompt_template,
                    "test_cases": test_cases
                },
                headers=self.headers
            ) as response:
                if response.status != 200:
                    raise AtuneError(f"Backtest request failed: {await response.text()}")
                return await response.json()

    async def generate_synthetic_data(
        self,
        schema: Dict[str, Any],
        count: int = 10,
        workflow_id: Optional[str] = None,
        **options
    ) -> List[Dict[str, Any]]:
        """
        Generate synthetic data based on a schema
        """
        _workflow_id = workflow_id or self.workflow_id
        if not _workflow_id:
            raise AtuneError("workflow_id must be provided")

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.api_url}/api/synthetic",
                json={
                    "workflow_id": _workflow_id,
                    "schema": schema,
                    "count": count,
                    "options": options
                },
                headers=self.headers
            ) as response:
                if response.status != 200:
                    raise AtuneError(f"Synthetic data generation failed: {await response.text()}")
                return await response.json()

    def monitor(self, input_content: Any, output_content: Any, **options):
        """
        Synchronous wrapper for audit
        """
        return asyncio.run(self.audit(input_content, output_content, **options))

    def visualize(self, port: int = 8501):
        """
        Start the visualization server
        """
        start_visualization_server(
            self.api_key,
            self.api_url,
            self.workflow_id,
            port
        )

    async def get_metrics(
        self,
        workflow_id: Optional[str] = None,
        timeframe: str = "24h"
    ) -> Dict[str, Any]:
        """
        Get metrics for a workflow
        """
        _workflow_id = workflow_id or self.workflow_id
        if not _workflow_id:
            raise AtuneError("workflow_id must be provided")

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.api_url}/api/metrics/{_workflow_id}",
                params={"timeframe": timeframe},
                headers=self.headers
            ) as response:
                if response.status != 200:
                    raise AtuneError(f"Metrics request failed: {await response.text()}")
                return await response.json()