# README

This is a simple app to visualize stock correlation.

## Usage

## Development

## Deployment

The deployment relies on containerization (with docker) and google cloud Platform (GCP) for hosting the container.

!!! info "Env variables"

    ```bash
    GCP_PROJECT_ID=correlator-453922
    GCP_REGION=us-west1
    CR_NAMESPACE=correlator
    IMAGE_NAME=correlator
    TAG=latest
    SERVICE_NAME=correlator
    ```

### GCP authentication

```bash
gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev
```

### Create image and push to GCP

```bash
docker build -t ${IMAGE_NAME} .
docker tag ${IMAGE_NAME}:${TAG} ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${CR_NAMESPACE}/${IMAGE_NAME}:${TAG}
docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${CR_NAMESPACE}/${IMAGE_NAME}:${TAG}
```

### Deploy to GCP

```bash
gcloud run deploy ${SERVICE_NAME} \
  --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT_ID}/${CR_NAMESPACE}/${IMAGE_NAME} \
  --platform managed \
  --region ${GCP_REGION} \
  --allow-unauthenticated \
  --port 8080 \
  --memory 2Gi \
  --cpu 4 \
  --min-instances 1
```
