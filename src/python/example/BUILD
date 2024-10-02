load("@bazel_skylib//rules:copy_file.bzl", "copy_file")

py_binary(
    name = "example",
    srcs = ["example.py"],
    data = [
        ":mm_service_plugin",
    ],
    deps = [
        "//src/interface:py_interfaces",
        "@zed_python_cpp//src/python/service_client",
        "@zed_python_cpp//src/python/service_probe",
    ],
)

copy_file(
    name = "mm_service_plugin",
    src = "//src/cpp/service_factory/mm_service_factory:ZMmServiceFactoryRunTimePlugin",
    out = "service_plugins/ZMmServiceFactoryRunTimePlugin.so",
    allow_symlink = True,
)

py_test(
    name = "test_mm_service",
    srcs = ["test_mm_service.py"],
    data = [
        ":mm_service_plugin",
    ],
    deps = [
        "//src/interface:py_interfaces",
        "@zed_python_cpp//src/python/service_client",
        "@zed_python_cpp//src/python/service_probe",
    ],
)
