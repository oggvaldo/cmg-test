variable "appId" {
  description = "Azure Kubernetes Service Cluster service principal"
}

variable "password" {
  description = "Azure Kubernetes Service Cluster password"
}

variable "resource_group_name"{
  type        = string 
  description = "Name of resource group"
}

variable "kubernetes_cluster_name"{
  type        = string 
  description = "Name of resource group"
}