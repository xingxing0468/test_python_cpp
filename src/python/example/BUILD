load("@bazel_skylib//rules:copy_file.bzl", "copy_file")

py_binary(
    name = "example",
    srcs = ["example.py"],
    deps = [
        "//src/interface:py_interfaces",
        "@z_python_cpp//src/python/service_channel:ipc_service_channel",
    ],
)

py_test(
    name = "test_mm_service",
    srcs = ["test_mm_service.py"],
    deps = [
        "//src/interface:py_interfaces",
        "@z_python_cpp//src/python/service_channel:ipc_service_channel",
    ],
)
