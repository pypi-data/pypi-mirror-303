# ModelPseudoLabelWorkers

Types:

```python
from lastmile.types import ModelPseudoLabelWorkerExecutePseudoLabelJobResponse
```

Methods:

- <code title="post /api/2/auto_eval/model_pseudo_label_worker/execute_pseudo_label_job">client.model_pseudo_label_workers.<a href="./src/lastmile/resources/model_pseudo_label_workers.py">execute_pseudo_label_job</a>(\*\*<a href="src/lastmile/types/model_pseudo_label_worker_execute_pseudo_label_job_params.py">params</a>) -> <a href="./src/lastmile/types/model_pseudo_label_worker_execute_pseudo_label_job_response.py">ModelPseudoLabelWorkerExecutePseudoLabelJobResponse</a></code>

# ModelFineTuneWorkers

Types:

```python
from lastmile.types import ModelFineTuneWorkerExecuteFineTuneJobResponse
```

Methods:

- <code title="post /api/2/auto_eval/model_fine_tune_worker/execute_fine_tune_job">client.model_fine_tune_workers.<a href="./src/lastmile/resources/model_fine_tune_workers.py">execute_fine_tune_job</a>(\*\*<a href="src/lastmile/types/model_fine_tune_worker_execute_fine_tune_job_params.py">params</a>) -> <a href="./src/lastmile/types/model_fine_tune_worker_execute_fine_tune_job_response.py">ModelFineTuneWorkerExecuteFineTuneJobResponse</a></code>

# Datasets

Types:

```python
from lastmile.types import (
    DatasetCreateResponse,
    DatasetListResponse,
    DatasetFinalizeSingleFileUploadResponse,
    DatasetGetResponse,
    DatasetGetViewResponse,
    DatasetRefineLabelsResponse,
    DatasetUploadFileResponse,
    DatasetUploadSplitFilesResponse,
)
```

Methods:

- <code title="post /api/2/auto_eval/dataset/create">client.datasets.<a href="./src/lastmile/resources/datasets.py">create</a>(\*\*<a href="src/lastmile/types/dataset_create_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_create_response.py">DatasetCreateResponse</a></code>
- <code title="post /api/2/auto_eval/dataset/list">client.datasets.<a href="./src/lastmile/resources/datasets.py">list</a>(\*\*<a href="src/lastmile/types/dataset_list_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="post /api/2/auto_eval/dataset/finalize_single_file_upload">client.datasets.<a href="./src/lastmile/resources/datasets.py">finalize_single_file_upload</a>(\*\*<a href="src/lastmile/types/dataset_finalize_single_file_upload_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_finalize_single_file_upload_response.py">DatasetFinalizeSingleFileUploadResponse</a></code>
- <code title="post /api/2/auto_eval/dataset/get">client.datasets.<a href="./src/lastmile/resources/datasets.py">get</a>(\*\*<a href="src/lastmile/types/dataset_get_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_get_response.py">DatasetGetResponse</a></code>
- <code title="post /api/2/auto_eval/dataset/get_view">client.datasets.<a href="./src/lastmile/resources/datasets.py">get_view</a>(\*\*<a href="src/lastmile/types/dataset_get_view_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_get_view_response.py">DatasetGetViewResponse</a></code>
- <code title="post /api/2/auto_eval/dataset/refine_labels">client.datasets.<a href="./src/lastmile/resources/datasets.py">refine_labels</a>(\*\*<a href="src/lastmile/types/dataset_refine_labels_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_refine_labels_response.py">DatasetRefineLabelsResponse</a></code>
- <code title="post /api/2/auto_eval/dataset/upload_file">client.datasets.<a href="./src/lastmile/resources/datasets.py">upload_file</a>(\*\*<a href="src/lastmile/types/dataset_upload_file_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_upload_file_response.py">DatasetUploadFileResponse</a></code>
- <code title="post /api/2/auto_eval/dataset/upload_split_files">client.datasets.<a href="./src/lastmile/resources/datasets.py">upload_split_files</a>(\*\*<a href="src/lastmile/types/dataset_upload_split_files_params.py">params</a>) -> <a href="./src/lastmile/types/dataset_upload_split_files_response.py">DatasetUploadSplitFilesResponse</a></code>

# Deployments

Types:

```python
from lastmile.types import DeploymentDeployInferenceEndpointResponse
```

Methods:

- <code title="post /api/2/auto_eval/deployment/deploy_inference_endpoint">client.deployments.<a href="./src/lastmile/resources/deployments.py">deploy_inference_endpoint</a>(\*\*<a href="src/lastmile/types/deployment_deploy_inference_endpoint_params.py">params</a>) -> <a href="./src/lastmile/types/deployment_deploy_inference_endpoint_response.py">DeploymentDeployInferenceEndpointResponse</a></code>

# Evaluations

Types:

```python
from lastmile.types import (
    EvaluationEvaluateResponse,
    EvaluationEvaluateDatasetResponse,
    EvaluationListMetricsResponse,
)
```

Methods:

- <code title="post /api/2/auto_eval/evaluation/evaluate">client.evaluations.<a href="./src/lastmile/resources/evaluations.py">evaluate</a>(\*\*<a href="src/lastmile/types/evaluation_evaluate_params.py">params</a>) -> <a href="./src/lastmile/types/evaluation_evaluate_response.py">EvaluationEvaluateResponse</a></code>
- <code title="post /api/2/auto_eval/evaluation/evaluate_dataset">client.evaluations.<a href="./src/lastmile/resources/evaluations.py">evaluate_dataset</a>(\*\*<a href="src/lastmile/types/evaluation_evaluate_dataset_params.py">params</a>) -> <a href="./src/lastmile/types/evaluation_evaluate_dataset_response.py">EvaluationEvaluateDatasetResponse</a></code>
- <code title="post /api/2/auto_eval/evaluation/list_metrics">client.evaluations.<a href="./src/lastmile/resources/evaluations.py">list_metrics</a>() -> <a href="./src/lastmile/types/evaluation_list_metrics_response.py">EvaluationListMetricsResponse</a></code>

# FineTuneJobs

Types:

```python
from lastmile.types import (
    FineTuneJobCreateResponse,
    FineTuneJobConfigureResponse,
    FineTuneJobGetStatusResponse,
    FineTuneJobSubmitResponse,
)
```

Methods:

- <code title="post /api/2/auto_eval/fine_tune_job/create">client.fine_tune_jobs.<a href="./src/lastmile/resources/fine_tune_jobs.py">create</a>(\*\*<a href="src/lastmile/types/fine_tune_job_create_params.py">params</a>) -> <a href="./src/lastmile/types/fine_tune_job_create_response.py">FineTuneJobCreateResponse</a></code>
- <code title="put /api/2/auto_eval/fine_tune_job/configure">client.fine_tune_jobs.<a href="./src/lastmile/resources/fine_tune_jobs.py">configure</a>(\*\*<a href="src/lastmile/types/fine_tune_job_configure_params.py">params</a>) -> <a href="./src/lastmile/types/fine_tune_job_configure_response.py">FineTuneJobConfigureResponse</a></code>
- <code title="post /api/2/auto_eval/fine_tune_job/get_status">client.fine_tune_jobs.<a href="./src/lastmile/resources/fine_tune_jobs.py">get_status</a>(\*\*<a href="src/lastmile/types/fine_tune_job_get_status_params.py">params</a>) -> <a href="./src/lastmile/types/fine_tune_job_get_status_response.py">FineTuneJobGetStatusResponse</a></code>
- <code title="post /api/2/auto_eval/fine_tune_job/submit">client.fine_tune_jobs.<a href="./src/lastmile/resources/fine_tune_jobs.py">submit</a>(\*\*<a href="src/lastmile/types/fine_tune_job_submit_params.py">params</a>) -> <a href="./src/lastmile/types/fine_tune_job_submit_response.py">FineTuneJobSubmitResponse</a></code>

# Models

Types:

```python
from lastmile.types import ModelRetrieveResponse, ModelListResponse
```

Methods:

- <code title="post /api/2/auto_eval/model/get">client.models.<a href="./src/lastmile/resources/models.py">retrieve</a>(\*\*<a href="src/lastmile/types/model_retrieve_params.py">params</a>) -> <a href="./src/lastmile/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="post /api/2/auto_eval/model/list">client.models.<a href="./src/lastmile/resources/models.py">list</a>(\*\*<a href="src/lastmile/types/model_list_params.py">params</a>) -> <a href="./src/lastmile/types/model_list_response.py">ModelListResponse</a></code>

# PseudoLabelJobs

Types:

```python
from lastmile.types import (
    PseudoLabelJobCreateResponse,
    PseudoLabelJobConfigureResponse,
    PseudoLabelJobGetStatusResponse,
    PseudoLabelJobSubmitResponse,
)
```

Methods:

- <code title="post /api/2/auto_eval/pseudo_label_job/create">client.pseudo_label_jobs.<a href="./src/lastmile/resources/pseudo_label_jobs.py">create</a>(\*\*<a href="src/lastmile/types/pseudo_label_job_create_params.py">params</a>) -> <a href="./src/lastmile/types/pseudo_label_job_create_response.py">PseudoLabelJobCreateResponse</a></code>
- <code title="put /api/2/auto_eval/pseudo_label_job/configure">client.pseudo_label_jobs.<a href="./src/lastmile/resources/pseudo_label_jobs.py">configure</a>(\*\*<a href="src/lastmile/types/pseudo_label_job_configure_params.py">params</a>) -> <a href="./src/lastmile/types/pseudo_label_job_configure_response.py">PseudoLabelJobConfigureResponse</a></code>
- <code title="post /api/2/auto_eval/pseudo_label_job/get_status">client.pseudo_label_jobs.<a href="./src/lastmile/resources/pseudo_label_jobs.py">get_status</a>(\*\*<a href="src/lastmile/types/pseudo_label_job_get_status_params.py">params</a>) -> <a href="./src/lastmile/types/pseudo_label_job_get_status_response.py">PseudoLabelJobGetStatusResponse</a></code>
- <code title="post /api/2/auto_eval/pseudo_label_job/submit">client.pseudo_label_jobs.<a href="./src/lastmile/resources/pseudo_label_jobs.py">submit</a>(\*\*<a href="src/lastmile/types/pseudo_label_job_submit_params.py">params</a>) -> <a href="./src/lastmile/types/pseudo_label_job_submit_response.py">PseudoLabelJobSubmitResponse</a></code>
