# -*- coding: utf-8 -*-
# Deployment settings for Stage2.
# This file is autogenerated by the mkb system and used by the s3e deployment
# tool during the build process.

config = {}
cmdline = ['D:/Marmalade/7.8/s3e/makefile_builder/mkb.py', 'd:/marm/Stage2/Stage2.mkb', '--default-buildenv=vc12x', '--msvc-project', '--deploy-only']
mkb = 'd:/marm/Stage2/Stage2.mkb'
mkf = ['d:\\marmalade\\7.8\\s3e\\s3e-default.mkf', 'd:\\marmalade\\7.8\\extensions\\s3eamazonads\\s3eamazonads.mkf', 'd:\\marmalade\\7.8\\modules\\iwutil\\iwutil.mkf', 'd:\\marmalade\\7.8\\modules\\third_party\\libjpeg\\libjpeg.mkf', 'd:\\marmalade\\7.8\\modules\\third_party\\libpng\\libpng.mkf', 'd:\\marmalade\\7.8\\modules\\third_party\\zlib\\zlib.mkf', 'd:\\marmalade\\7.8\\platform_libs\\android\\amazon-ads-android-sdk\\amazon-ads-android-sdk.mkf', 'd:\\marmalade\\7.8\\platform_libs\\iphone\\amazon-ads-ios-sdk\\amazon-ads-ios-sdk.mkf', 'd:\\marmalade\\7.8\\modules\\iw2d\\iw2d.mkf', 'd:\\marmalade\\7.8\\modules\\iwgx\\iwgx.mkf', 'd:\\marmalade\\7.8\\modules\\iwgl\\iwgl.mkf', 'd:\\marmalade\\7.8\\modules\\iwgeom\\iwgeom.mkf', 'd:\\marmalade\\7.8\\modules\\iwresmanager\\iwresmanager.mkf', 'd:\\marmalade\\7.8\\extensions\\pvrtextool\\pvrtextool.mkf', 'd:\\marmalade\\7.8\\modules\\iwgxfont\\iwgxfont.mkf', 'd:\\marmalade\\7.8\\modules\\third_party\\tiniconv\\tiniconv.mkf', 'd:\\marm\\stage2\\modules\\soundengine\\soundengine.mkf']

class DeployConfig(object):
    pass

######### ASSET GROUPS #############

assets = {}

assets['Default'] = [
    ('d:/marm/Stage2/data/textures', 'textures', 0),
    ('d:/marm/Stage2/data/audio', 'audio', 0),
]

######### DEFAULT CONFIG #############

class DefaultConfig(DeployConfig):
    embed_icf = -1
    name = 'Stage2'
    pub_sign_key = 0
    priv_sign_key = 0
    caption = 'Stage2'
    long_caption = 'Stage2'
    version = [0, 0, 1]
    config = ['d:/marm/Stage2/data/app.icf']
    data_dir = 'd:/marm/Stage2/data'
    mkb_dir = 'd:/marm/Stage2'
    iphone_link_lib = ['s3eAmazonAds']
    osx_ext_dll = ['d:/marmalade/7.8/extensions/pvrtextool/lib/osx/libPVRTexTool.dylib']
    wp81_extra_pri = []
    ws8_ext_capabilities = []
    ws8_ext_native_only_dll = []
    ws81_ext_native_only_dll = []
    android_external_res = []
    win32_ext_dll = ['d:/marmalade/7.8/extensions/pvrtextool/lib/win32/PVRTexTool.dll']
    wp8_ext_capabilities = []
    ws8_extra_res = []
    ws81_ext_managed_dll = []
    iphone_link_libdir = ['d:/marmalade/7.8/extensions/s3eamazonads/lib/iphone']
    android_extra_application_manifest = ['d:/marmalade/7.8/extensions/s3eamazonads/source/android/ExtraAppManifests.xml']
    ws8_ext_native_dll = []
    android_external_assets = []
    blackberry_extra_descriptor = []
    android_ext_target_sdk_version = [17]
    android_extra_manifest = []
    wp81_ext_sdk_ref = []
    iphone_link_libdirs = []
    wp81_ext_device_capabilities = []
    linux_ext_lib = []
    android_ext_min_sdk_version = [4]
    wp81_ext_native_only_dll = []
    ws8_ext_managed_dll = []
    ws8_ext_sdk_manifest_part = []
    ws8_ext_device_capabilities = []
    ws81_extra_pri = []
    android_external_jars = ['d:/marmalade/7.8/platform_libs/android/amazon-ads-android-sdk/third_party/lib/amazon-ads-5.4.235.jar', 'd:/marmalade/7.8/extensions/s3eamazonads/lib/android/s3eAmazonAds.jar']
    win8_winrt_extra_res = []
    wp81_ext_sdk_manifest_part = []
    android_supports_gl_texture = []
    wp81_extra_res = []
    wp81_ext_managed_dll = []
    wp81_ext_capabilities = []
    iphone_extra_plist = []
    ws81_ext_sdk_manifest_part = []
    ws81_ext_device_capabilities = []
    ws8_ext_sdk_ref = []
    iphone_extra_string = []
    tizen_so = []
    wp8_ext_native_dll = []
    win8_phone_extra_res = []
    win32_aux_dll = []
    win8_store_extra_res = []
    iphone_link_opts = ['-Fd:/marmalade/7.8/platform_libs/iphone/amazon-ads-ios-sdk/third_party/Ads -framework AmazonAd', '-weak_framework AdSupport -weak_framework CoreLocation -weak_framework SystemConfiguration', '-weak_framework CoreTelephony -weak_framework MediaPlayer', '-weak_framework EventKit -weak_framework EventKitUI']
    ws81_ext_sdk_ref = []
    wp8_extra_res = []
    ws81_ext_native_dll = []
    ws8_extra_pri = []
    wp8_ext_managed_dll = []
    android_extra_packages = []
    android_so = ['d:/marmalade/7.8/extensions/s3eamazonads/lib/android/libs3eAmazonAds.so']
    wp8_ext_sdk_ref = []
    osx_extra_res = []
    ws81_extra_res = []
    wp81_ext_native_dll = []
    ws81_ext_capabilities = []
    iphone_link_libs = []
    android_extra_strings = []
    target = {
         'mips' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_mips/Stage2.so',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_mips/Stage2.so',
                 },
         'gcc_x86' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_x86/Stage2.so',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_x86/Stage2.so',
                 },
         'gcc_x86_tizen' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_x86_tizen/Stage2.s86',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_x86_tizen/Stage2.s86',
                 },
         'firefoxos' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_firefoxos/Stage2.js',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_firefoxos/Stage2.js',
                 },
         'mips_gcc' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_mips/Stage2.so',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_mips/Stage2.so',
                 },
         'arm_gcc' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_arm/Stage2.s3e',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_arm/Stage2.s3e',
                 },
         'naclx86_64' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_naclx86_64/Stage2.so.s64',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_naclx86_64/Stage2.so.s64',
                 },
         'aarch64_gcc' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_aarch64/Stage2.s3e',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_aarch64/Stage2.s3e',
                 },
         'gcc_x86_android' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_gcc_x86_android/Stage2.so',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_gcc_x86_android/Stage2.so',
                 },
         'arm' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_arm/Stage2.s3e',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_arm/Stage2.s3e',
                 },
         'x86' : {
                   'debug'   : r'd:/marm/Stage2/build_stage2_vc12x/Debug_Stage2_VC12X_x86/Stage2.s86',
                   'release' : r'd:/marm/Stage2/build_stage2_vc12x/Release_Stage2_VC12X_x86/Stage2.s86',
                 },
        }
    arm_arch = ''
    assets_original = assets
    assets = assets['Default']

default = DefaultConfig()
