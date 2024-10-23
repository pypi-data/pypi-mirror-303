from gladier_tools.experimental.globus import GlobusMkDir
from gladier import GladierBaseClient, generate_flow_definition


def test_mkdir_tool():
    mkdir_tool = GlobusMkDir(state_name="testMkDirState")
    flow_def = mkdir_tool.get_flow_definition()
    assert "testMkDirState" in flow_def["States"]
    inputs = mkdir_tool.required_input
    assert "mkdir_endpoint_id" in inputs
    assert "mkdir_path" in inputs

    @generate_flow_definition
    class TestGladierClient(GladierBaseClient):
        gladier_tools = [mkdir_tool]

    test_client = TestGladierClient()

    fd = test_client.get_flow_definition()
    assert "testMkDirState" in fd["States"]
