#ifndef _Z_MM_SERVICE_FACTORY_H_
#define _Z_MM_SERVICE_FACTORY_H_

#include <IServiceFactory.h>

#include "src/cpp/service_implementation/mm_service/ZMmService.h"

class ZMmServiceFactory : public IServiceFactory {
 public:
  std::shared_ptr<google::protobuf::Service> GenerateServiceInstance()
      override {
    return std::make_shared<ZMmService>();
  }
};

#endif