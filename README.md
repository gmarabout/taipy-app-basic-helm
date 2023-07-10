# Taipy-app-basic-helm

This project shows how to deploy a basic Taipy app to Kubernetes using Helm.

## Prerequisites

* Have a local Kubernetes cluster running with Docker Desktop or Minikube. 
* Have Helm installed.

## Usage

1. Create the docker image for the Taipy app:

```
$ docker build -t my-taipy-app:1.0.0 .
```

2. Deploy the Helm chart using:
```
$ helm install my-release deployment/
```

3. Open the app on `http://localhost:5000`
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE.md`](LICENSE.md).

