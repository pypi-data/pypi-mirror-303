import subprocess
from mxl.config import config
from mxl.installer import command
from mxl.installer._bootstrap import _bootstrap


@command('run', '...',
         """Executes the command line but forces the initialization of the agent
         automatically at startup.

         If using an agent configuration file, the path to the file should be
         supplied by the environment variable MXL_CONFIG_FILE.""")
def run(args):
    if len(args) == 0:
        print("Expected args are missing.")
        return

    exporters = [
        "--traces_exporter otlp" if config.collect_traces else "--traces_exporter none",
        "--metrics_exporter otlp" if config.collect_metrics else "--metrics_exporter none",
        "--logs_exporter otlp" if config.collect_logs else "--logs_exporter none"
    ]

    # cmd1 = "mxl-bootstrap -a install"
    cmd2 = f"mxl-instrument {' '.join(exporters)} \
    --tracer_provider sdk_tracer_provider \
    --exporter_otlp_endpoint {config.exporter_otlp_endpoint} \
    --resource_attributes={config.resource_attributes} \
    --service_name {config.service_name} \
    --propagators {config.otel_propagators} {' '.join(args)}"

    _bootstrap()

    try:
        subprocess.run(cmd2, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed instrumenting with error: {e}")
