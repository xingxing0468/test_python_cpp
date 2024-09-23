#include "src/cpp/service_implementation/mm_service/ZMmService.h"

#include <stdio.h>

#include "src/cpp/mm/ZMm.h"

void ZMmService::GetMmGeos(google::protobuf::RpcController* controller,
                           const mm::MmFilterInputT* request,
                           mm::GeoCollectionT* response,
                           google::protobuf::Closure* done) {
  printf("GetMmGeos in CPP, request: \n [%s]\n",
         request->DebugString().c_str());

  const MmTypeT mm_type{static_cast<MmTypeT>(request->type())};
  const auto mms = request->mms();

  MmCollectionT ms{};
  for (const auto& mm : mms) {
    GeoT geometry{mm.geometry().height(), mm.geometry().length()};
    ms.push_back({geometry, static_cast<MmTypeT>(mm.type())});
  }
  const auto ret_mms = FilterMm(ms, mm_type);

  for (const auto& ret_mm : ret_mms) {
    auto new_mm_geos = response->add_ret_geos();
    new_mm_geos->set_height(ret_mm.height);
    new_mm_geos->set_length(ret_mm.length);
  }
  printf("FilterEnv in CPP, response: \n [%s]\n",
         response->DebugString().c_str());
  return;
}