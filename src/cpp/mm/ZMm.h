#ifndef _Z_MM_H_
#define _Z_MM_H_

#include <cstdint>
#include <tuple>
#include <unordered_map>
#include <vector>

constexpr float kMinX{-100.};
constexpr float kMaxX{100.};
constexpr float kMinY{-100.};
constexpr float kMaxY{100.};
constexpr std::uint32_t kScaleFactor{1000U};  // resolution support to 0.001

struct GeoT {
  GeoT(const float input_height, const float input_length)
      : height(input_height), length(input_length) {};
  float height{0.F};
  float length{0.F};
};

enum class MmTypeT : std::uint8_t {
  Fool = 0U,
  Normal = 1U,
  Size = 2U,
};

struct MmT {
  GeoT geometry;
  MmTypeT type;
};

using MmCollectionT = std::vector<MmT>;

std::vector<GeoT> FilterMm(const MmCollectionT& mms, const MmTypeT& type);

#endif