#include <pybind11/pybind11.h>
#include <string>
#include <CoreFoundation/CoreFoundation.h>
#include <objc/objc-runtime.h>

std::string bundleIdentifier = "org.python.PythonLauncher";

void injectBundleId(std::string identifier) {
    bundleIdentifier=identifier;
    class_replaceMethod(objc_getClass("NSBundle"), sel_registerName("bundleIdentifier"),
                        method_getImplementation((Method) ^ {
                                return CFStringCreateWithCString(nullptr, bundleIdentifier.c_str(), CFStringBuiltInEncodings::kCFStringEncodingUTF8);
                        }), nullptr);
}

PYBIND11_MODULE(injectionSupport,m){
    m.def("injectBundleIdentifier",&injectBundleId);
}
