provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "default" {
  name     = "cmg-test-rg"
  location = "East US"

  tags = {
    environment = "Test"
  }
}

resource "azurerm_kubernetes_cluster" "default" {
  name                = "cmg-test-aks"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  dns_prefix          = "cmg-test-k8s"

  default_node_pool {
    name            = "default"
    node_count      = 2
    vm_size         = "Standard_B2s"
    os_disk_size_gb = 30
  }

  service_principal {
    client_id     = var.appId
    client_secret = var.password
  }

  role_based_access_control {
    enabled = true
  }

  tags = {
    environment = "Test"
  }
}
