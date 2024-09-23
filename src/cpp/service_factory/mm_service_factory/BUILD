cc_library(
    name = "ZMmServiceFactory",
    srcs = ["ZMmServiceFactory.cpp"],
    hdrs = ["ZMmServiceFactory.h"],
    visibility = ["//src/cpp:__subpackages__"],
    deps = [
        "//src/cpp/service_implementation/mm_service:MmServicesImpl",
        "@zed_python_cpp//:cc_service_factory_common",
    ],
)

cc_library(
    name = "ZMmServiceFactoryRunTimeImpl",
    srcs = ["ZMmServiceFactoryImpl.cpp"],
    visibility = ["__subpackages__"],
    deps = [":ZMmServiceFactory"],
)

cc_shared_library(
    name = "ZMmServiceFactoryRunTimePlugin",
    roots = [":ZMmServiceFactoryRunTimeImpl"],
    visibility = ["//src:__subpackages__"],
)
