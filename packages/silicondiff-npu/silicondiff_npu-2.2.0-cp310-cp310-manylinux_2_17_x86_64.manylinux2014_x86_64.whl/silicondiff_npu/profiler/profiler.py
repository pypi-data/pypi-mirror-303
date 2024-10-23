import torch_npu


class profile:
    def __init__(
        self,
        *,
        chrome_trace=None,
        tensorboard_trace=None,
        profiler_level=0,
        record_shapes=False,
        profile_memory=False,
        with_stack=False,
        enable=True,
    ):
        self.chrome_trace = chrome_trace
        if not enable:
            self.prof = None
            return
        if profiler_level == 0:
            profiler_level = torch_npu.profiler.ProfilerLevel.Level0
        elif profiler_level == 1:
            profiler_level = torch_npu.profiler.ProfilerLevel.Level1
        elif profiler_level == 2:
            profiler_level = torch_npu.profiler.ProfilerLevel.Level2
        else:
            raise TypeError("profiler_level should be 0, 1 or 2")
        experimental_config = torch_npu.profiler._ExperimentalConfig(
            aic_metrics=torch_npu.profiler.AiCMetrics.PipeUtilization,
            profiler_level=profiler_level,
            l2_cache=False,
            data_simplification=False,
        )
        activities = [
            torch_npu.profiler.ProfilerActivity.CPU,
            torch_npu.profiler.ProfilerActivity.NPU,
        ]
        on_trace_ready = None
        if tensorboard_trace is not None:
            on_trace_ready = torch_npu.profiler.tensorboard_trace_handler(
                tensorboard_trace
            )
        self.prof = torch_npu.profiler.profile(
            activities=activities,
            on_trace_ready=on_trace_ready,
            record_shapes=record_shapes,
            profile_memory=profile_memory,
            with_stack=with_stack,
            experimental_config=experimental_config,
        )

    def __enter__(self):
        if self.prof is None:
            return
        self.prof.__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.prof is None:
            return
        self.prof.__exit__(exc_type, exc_value, traceback)
        if self.chrome_trace is not None:
            self.prof.export_chrome_trace(self.chrome_trace)
