# Copyright 2022 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dlrover.python.common.constants import PlatformType
from dlrover.python.scheduler.kubernetes import K8sElasticJob, K8sJobParams


def new_elastic_job(platform, job_name, namespace):
    if platform in (PlatformType.KUBERNETES, PlatformType.PY_KUBERNETES):
        return K8sElasticJob(job_name, namespace)
    else:
        raise ValueError("Not support engine %s", platform)


def new_job_params(platform, job_name, namespace):
    if platform in (PlatformType.KUBERNETES, PlatformType.PY_KUBERNETES):
        return K8sJobParams(platform, namespace, job_name)
    else:
        raise ValueError("Not support platform %s", platform)
