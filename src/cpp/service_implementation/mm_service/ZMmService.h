#ifndef _Z_EM_SERVICE_H_
#define _Z_EM_SERVICE_H_

#include "src/interface/IMmService.pb.h"

class ZMmService : public mm::Mm {
 public:
  // IEmService
  void GetMmGeos(google::protobuf::RpcController* controller,
                 const mm::MmFilterInputT* request,
                 mm::GeoCollectionT* response,
                 google::protobuf::Closure* done) override;
};

#endif