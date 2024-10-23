from io import BytesIO
from textwrap import dedent
from time import sleep

import pytest

from snowflake.core.exceptions import ConflictError, NotFoundError
from snowflake.core.service import JobService, ServiceCollection, ServiceSpecInlineText, ServiceSpecStageFile
from snowflake.core.service._service import ServiceResource
from tests.utils import random_string


RETRY_TIMES = 10


def wait_for_job_creation(job: ServiceResource):
    # wait for the job to be created if it is an async request otherwise fecth() below might fail if it is executed
    # before the job is created
    for _ in range(RETRY_TIMES):
        try:
            return job.fetch()
        except NotFoundError:
            sleep(1)
    raise Exception(f"Job creation failed: {job.name}")


@pytest.mark.min_sf_ver("8.34")
def test_execute_job_service(services: ServiceCollection, session, imagerepo, shared_compute_pool):
    # create a job from service spec in stage
    job_name = random_string(5, "test_job_")
    stage_name = random_string(5, "test_stage_")
    session.sql(f"create temp stage {stage_name};").collect()
    spec_file = "spec.yaml"
    stage_file = f"@{stage_name}"
    spec = f"{stage_file}/{spec_file}"
    session.file.put_stream(
        BytesIO(
            dedent(f"""\
                spec:
                  containers:
                  - name: hello-world
                    image: {imagerepo}/hello-world:latest
                """).encode()
        ),
        spec,
    )

    test_job_spec = JobService(
        name=job_name,
        compute_pool=shared_compute_pool,
        spec=ServiceSpecStageFile(stage=stage_name, spec_file=spec_file),
    )
    test_job = services.execute_job(test_job_spec, async_req=True)

    fetched_job = wait_for_job_creation(test_job)

    assert fetched_job.name.upper() == job_name.upper()
    assert fetched_job.compute_pool.upper() == shared_compute_pool.upper()
    assert fetched_job.min_instances == 1
    assert fetched_job.max_instances == 1
    assert fetched_job.database_name.upper() == services.database.name.upper()
    assert fetched_job.schema_name.upper() == services.schema.name.upper()

    # create a job with the same name and expect a conflict error
    with pytest.raises(
        ConflictError,
    ):
        services.execute_job(test_job_spec)

    # create a job from inline service spec
    inline_spec = dedent(
        f"""\
        spec:
          containers:
          - name: hello-world
            image: {imagerepo}/hello-world:latest
         """
    )
    test_job_inline_spec = JobService(
        name=job_name,
        compute_pool=shared_compute_pool,
        spec=ServiceSpecInlineText(spec_text=inline_spec),
    )
    test_job = services.execute_job(test_job_inline_spec, async_req=True)

    fetched_job_inline_spec = wait_for_job_creation(test_job)

    assert fetched_job_inline_spec.name.upper() == test_job_inline_spec.name.upper()
