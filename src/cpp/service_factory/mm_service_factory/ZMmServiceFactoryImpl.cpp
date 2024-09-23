#include "src/cpp/service_factory/mm_service_factory/ZMmServiceFactory.h"

extern "C" {
std::string GetServiceName() { return {"Mm"}; }

std::shared_ptr<IServiceFactory> GetServiceFactory() {
  return std::make_shared<ZMmServiceFactory>();
}
}