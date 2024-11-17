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

py_test(
    name = "test_mm_service_single_process",
    srcs = ["test_mm_service_single_process.py"],
    data = [
        ":mm_service_plugin",
    ],
    deps = [
        "//src/interface:py_interfaces",
        "@z_python_cpp//src/python/service_channel:local_service_channel",
    ],
)

copy_file(
    name = "mm_service_plugin",
    src = "//src/cpp/service_factory/mm_service_factory:ZMmServiceFactoryRunTimePlugin",
    out = "service_plugins/ZMmServiceFactoryRunTimePlugin.so",
    allow_symlink = True,
)
