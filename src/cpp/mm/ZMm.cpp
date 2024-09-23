#include "src/cpp/mm/ZMm.h"

std::vector<GeoT> FilterMm(const MmCollectionT& mms, const MmTypeT& type) {
  std::vector<GeoT> ret;

  for (const auto& mm : mms) {
    if (mm.type == type) {
      ret.push_back(mm.geometry);
    }
  }
  return ret;
}