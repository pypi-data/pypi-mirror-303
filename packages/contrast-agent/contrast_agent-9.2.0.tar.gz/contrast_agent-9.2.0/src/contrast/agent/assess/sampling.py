# Copyright © 2024 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.

from contrast.utils.decorators import fail_quietly
from contrast.utils.timer import now_ms
from dataclasses import dataclass
from collections.abc import Mapping

from contrast_vendor import structlog as logging

logger = logging.getLogger("contrast")

REQUESTS = dict()
LOGGED_SAMPLING_MESSAGE = False


@dataclass
class SamplerConfig:
    assess_enabled: bool
    sampler_enabled: bool
    window_ms: int
    baseline: int
    request_freq: int


def update_sampler_config(agent_config: Mapping):
    from contrast.agent import agent_state

    cfg = SamplerConfig(
        agent_config.get("assess.enable"),
        agent_config.get("assess.sampling.enable"),
        agent_config.get("assess.sampling.window_ms"),
        agent_config.get("assess.sampling.baseline"),
        agent_config.get("assess.sampling.request_frequency"),
    )

    agent_state.module.sampling_cfg = cfg


def _enabled(config: SamplerConfig):
    global LOGGED_SAMPLING_MESSAGE

    sampling_enabled = config.assess_enabled and config.sampler_enabled

    if not LOGGED_SAMPLING_MESSAGE and sampling_enabled:
        logger.info(
            "Contrast assess.sampling is enabled in your configuration. "
            "Not all requests will be analyzed."
        )
        LOGGED_SAMPLING_MESSAGE = True

    return sampling_enabled


# If we can't determine sampling, it's better to analyze the request.
@fail_quietly("Unable to determine sampling", False)
def meets_criteria(context, config: SamplerConfig) -> bool:
    """
    If a request meets criteria for sampling, agent should not analyze request.

    Criteria is met if request happens inside a sampling time window and request
    count minus baseline doesn't meet frequency setting.
    """
    if not _enabled(config):
        return False

    if context.hash is None:
        # If we cannot determine the uniqueness of this request, it's better
        # to analyze the request
        return False

    if context.hash in REQUESTS:
        history = REQUESTS[context.hash]
    else:
        history = REQUESTS[context.hash] = RequestHistory()

    history.hit()

    # if sampling window has been exceeded, reset it.
    if history.elapsed() >= config.window_ms:
        history.reset()
        return False

    # once hits exceed baseline setting, limit analysis based on frequency setting.
    baseline = config.baseline
    frequency = config.request_freq

    return not (history.hits <= baseline or (history.hits - baseline) % frequency == 0)


class RequestHistory:
    def __init__(self):
        self._start = now_ms()
        self._hit = 0

    @property
    def hits(self):
        return self._hit

    def elapsed(self):
        return now_ms() - self._start

    def hit(self):
        """Increment attempted requests, not analyzed requests"""
        self._hit += 1

    def reset(self):
        self._start = now_ms()
        self._hit = 1

    def __repr__(self):
        return f"Started at: {self._start} - Hit : {self._hit}"
