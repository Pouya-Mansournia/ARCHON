# Cloud Providers & Infrastructure

## Goal

Pick the cloud provider, core service categories, and infrastructure-as-code approach that match the team's actual skill set and the product's actual needs — provider choice is a long-term commitment (data gravity, egress costs, team expertise all compound), so it deserves deliberate evaluation, not default-to-whatever-the-founder-used-last-time.

## Provider Comparison — Full Detail

| Factor | AWS | GCP | Azure |
|---|---|---|---|
| Service breadth | Broadest, especially niche/specialized services | Strong but narrower than AWS; excels in data/ML | Strong but narrower than AWS; excels in enterprise/identity integration |
| Talent pool | Largest — easiest to hire for | Smaller than AWS, growing | Smaller than AWS, strong in enterprise/.NET shops |
| Pricing complexity | High — many SKUs, easy to overspend without discipline | Moderate, generally considered more straightforward billing | Moderate, complex enterprise licensing interplay (e.g., hybrid benefit) |
| Kubernetes | EKS — solid, more manual setup than GKE | GKE — most mature managed Kubernetes offering, autopilot mode | AKS — solid, improving rapidly |
| Data/Analytics/ML | Strong (Redshift, SageMaker) but more assembly required | Best-in-class (BigQuery, Vertex AI) — most "it just works" | Strong (Synapse, Azure ML), deep Microsoft data-tooling integration |
| Best-fit team profile | General-purpose, broad needs, largest community/support resources | Data-heavy or ML-heavy product, team comfortable with GCP's more opinionated tooling | Enterprise teams already on Microsoft stack (AD, Office 365, .NET) |

## Core Service Categories (Provider-Agnostic Concepts)

- **Compute** — VMs (EC2/Compute Engine/Azure VMs), containers (ECS/Fargate, GKE, AKS), serverless functions (Lambda, Cloud Functions, Azure Functions). Default to managed container compute (Fargate-style) for most application workloads — it avoids both raw VM management overhead and premature full-Kubernetes complexity.
- **Networking** — VPC/VNet, subnets, security groups/firewall rules, load balancers, CDN. Get the network security boundary right early (private subnets for databases, public only for what truly needs internet ingress) — retrofitting network segmentation onto a live system is painful.
- **Managed databases** — RDS/Cloud SQL/Azure Database, with automated backups, read replicas, and failover handled by the provider. Strongly prefer managed database services over self-hosting a database on a VM unless there's a specific, justified reason (cost at extreme scale, a specific feature the managed offering lacks).
- **Identity & access management** — IAM roles/policies (AWS), IAM (GCP), Azure AD/Entra ID. Apply least-privilege from day one; retrofitting IAM discipline onto an already-sprawling set of overly-permissive roles is a recurring real-world security cleanup project.

## Infrastructure as Code

| Tool | Best for |
|---|---|
| Terraform | Provider-agnostic, broadest community/module ecosystem, the safe default choice |
| Pulumi | Teams wanting to write infra in a general-purpose language (TypeScript, Python, Go) rather than HCL |
| AWS CDK / Azure Bicep | Teams fully committed to a single cloud, wanting tighter native integration |
| ClickOps (manual console) | Acceptable only for the earliest prototype stage — should not persist past initial validation |

**Decision rule:** Use Terraform by default. Move off ClickOps as soon as there's a second environment (staging) to keep in sync with production — manual console configuration drift between environments is a common and entirely avoidable source of "works in staging, breaks in prod" incidents.

## Common Mistakes

- Choosing a cloud provider based on credits/promotional pricing alone rather than long-term fit, then facing painful migration costs once credits expire.
- Self-hosting a database on a raw VM to "save money" without budgeting the operational burden (patching, backup verification, failover testing) that the managed service would have absorbed.
- Letting infrastructure configuration drift via manual console changes once more than one environment exists, with no IaC source of truth.
- Over-broad IAM roles ("just give it admin, we'll fix it later") that never actually get tightened later.
