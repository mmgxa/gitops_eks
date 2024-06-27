<div align="center">

# Canary Deployment via GitOps using Argo CD on EKS

</div>

# Overview
In this repository, we deploy multiple models via canary deployment on EKS. Argo CD is used to deploy these models.

Make sure the following tools are installed
- eksctl
- kubectl
- helm
- kustomize
- argo CLI

# Steps

Create an Argo application:
```bash
kubectl apply -f 03_argo_app.yaml
```

This will deploy our first model. We will run an infinite loop for inference to see the results

```bash
while true; do python 04_test.py ; done
```

To deploy next version of our deployment/inference service, we can make changes to our git repository.

```bash
git add models/b_age_30.yaml; git commit -m "added modelb"; git push -u origin main
```

# Inference Demo

[![Demo](https://img.youtube.com/vi/SKaYIaQ7OPU/hqdefault.jpg)](https://www.youtube.com/embed/SKaYIaQ7OPU)
