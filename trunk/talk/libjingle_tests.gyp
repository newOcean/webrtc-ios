#
# libjingle
# Copyright 2012, Google Inc.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#  3. The name of the author may not be used to endorse or promote products
#     derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

{
  'includes': ['build/common.gypi'],
  'targets': [
    {
      # TODO(ronghuawu): Use gtest.gyp from chromium.
      'target_name': 'gunit',
      'type': 'static_library',
      'sources': [
        '<(DEPTH)/testing/gtest/src/gtest-all.cc',
      ],
      'include_dirs': [
        '<(DEPTH)/testing/gtest/include',
        '<(DEPTH)/testing/gtest',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/testing/gtest/include',
        ],
      },
      'conditions': [
        ['OS=="android"', {
          'include_dirs': [
            '<(android_ndk_include)',
          ]
        }],
      ],
    },  # target gunit
    {
      'target_name': 'libjingle_unittest_main',
      'type': 'static_library',
      'dependencies': [
        '<(DEPTH)/third_party/libyuv/libyuv.gyp:libyuv',
        'gunit',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/third_party/libyuv/include',
        ],
      },
      'sources': [
        'base/unittest_main.cc',
        # Also use this as a convenient dumping ground for misc files that are
        # included by multiple targets below.
        'base/fakecpumonitor.h',
        'base/fakenetwork.h',
        'base/fakesslidentity.h',
        'base/faketaskrunner.h',
        'base/gunit.h',
        'base/testbase64.h',
        'base/testechoserver.h',
        'base/win32toolhelp.h',
        'media/base/fakecapturemanager.h',
        'media/base/fakemediaengine.h',
        'media/base/fakemediaprocessor.h',
        'media/base/fakenetworkinterface.h',
        'media/base/fakertp.h',
        'media/base/fakevideocapturer.h',
        'media/base/fakevideorenderer.h',
        'media/base/nullvideoframe.h',
        'media/base/nullvideorenderer.h',
        'media/base/testutils.cc',
        'media/base/testutils.h',
        'media/devices/fakedevicemanager.h',
        'media/webrtc/fakewebrtccommon.h',
        'media/webrtc/fakewebrtcdeviceinfo.h',
        'media/webrtc/fakewebrtcvcmfactory.h',
        'media/webrtc/fakewebrtcvideocapturemodule.h',
        'media/webrtc/fakewebrtcvideoengine.h',
        'media/webrtc/fakewebrtcvoiceengine.h',
      ],
    },  # target libjingle_unittest_main

    {
      'target_name': 'libjingle_sound_unittest',
      'type': 'executable',
      'dependencies': [
        'gunit',
        'libjingle.gyp:libjingle_sound',
        'libjingle_unittest_main',
      ],
      'sources': [
        'sound/automaticallychosensoundsystem_unittest.cc',
      ],
    },  # target libjingle_sound_unittest
  
    {
      'target_name': 'libjingle_p2p_unittest',
      'type': 'executable',
      'dependencies': [
        '<(DEPTH)/third_party/libsrtp/libsrtp.gyp:libsrtp',
        'gunit',
        'libjingle.gyp:libjingle',
        'libjingle.gyp:libjingle_p2p',
        'libjingle_unittest_main',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/libsrtp/srtp',
      ],
      'sources': [
        'p2p/base/dtlstransportchannel_unittest.cc',
        'p2p/base/fakesession.h',
        'p2p/base/p2ptransportchannel_unittest.cc',
        'p2p/base/port_unittest.cc',
        'p2p/base/portallocatorsessionproxy_unittest.cc',
        'p2p/base/pseudotcp_unittest.cc',
        'p2p/base/relayport_unittest.cc',
        'p2p/base/relayserver_unittest.cc',
        'p2p/base/session_unittest.cc',
        'p2p/base/stun_unittest.cc',
        'p2p/base/stunport_unittest.cc',
        'p2p/base/stunrequest_unittest.cc',
        'p2p/base/stunserver_unittest.cc',
        'p2p/base/testrelayserver.h',
        'p2p/base/teststunserver.h',
        'p2p/base/testturnserver.h',
        'p2p/base/transport_unittest.cc',
        'p2p/base/transportdescriptionfactory_unittest.cc',
        'p2p/client/connectivitychecker_unittest.cc',
        'p2p/client/fakeportallocator.h',
        'p2p/client/portallocator_unittest.cc',
        'session/media/channel_unittest.cc',
        'session/media/channelmanager_unittest.cc',
        'session/media/currentspeakermonitor_unittest.cc',
        'session/media/mediarecorder_unittest.cc',
        'session/media/mediamessages_unittest.cc',
        'session/media/mediasession_unittest.cc',
        'session/media/mediasessionclient_unittest.cc',
        'session/media/rtcpmuxfilter_unittest.cc',
        'session/media/srtpfilter_unittest.cc',
        'session/media/ssrcmuxfilter_unittest.cc',
      ],
      'conditions': [
        ['OS=="win"', {
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                'strmiids.lib',
              ],
            },
          },
        }],
      ],
    },  # target libjingle_p2p_unittest
    {
      'target_name': 'libjingle_peerconnection_unittest',
      'type': 'executable',
      'dependencies': [
        'gunit',
        'libjingle.gyp:libjingle',
        'libjingle.gyp:libjingle_p2p',
        'libjingle.gyp:libjingle_peerconnection',
        'libjingle_unittest_main',
      ],
      # TODO(ronghuawu): Reenable below unit tests that require gmock.
      'sources': [
        'app/webrtc/datachannel_unittest.cc',
        'app/webrtc/dtmfsender_unittest.cc',
        'app/webrtc/jsepsessiondescription_unittest.cc',
        'app/webrtc/localaudiosource_unittest.cc',
        'app/webrtc/localvideosource_unittest.cc',
        # 'app/webrtc/mediastream_unittest.cc',
        # 'app/webrtc/mediastreamhandler_unittest.cc',
        'app/webrtc/mediastreamsignaling_unittest.cc',
        'app/webrtc/peerconnection_unittest.cc',
        'app/webrtc/peerconnectionfactory_unittest.cc',
        'app/webrtc/peerconnectioninterface_unittest.cc',
        # 'app/webrtc/peerconnectionproxy_unittest.cc',
        'app/webrtc/test/fakeaudiocapturemodule.cc',
        'app/webrtc/test/fakeaudiocapturemodule.h',
        'app/webrtc/test/fakeaudiocapturemodule_unittest.cc',
        'app/webrtc/test/fakeconstraints.h',
        'app/webrtc/test/fakedtlsidentityservice.h',
        'app/webrtc/test/fakemediastreamsignaling.h',
        'app/webrtc/test/fakeperiodicvideocapturer.h',
        'app/webrtc/test/fakevideotrackrenderer.h',
        'app/webrtc/test/mockpeerconnectionobservers.h',
        'app/webrtc/test/testsdpstrings.h',
        'app/webrtc/videotrack_unittest.cc',
        'app/webrtc/webrtcsdp_unittest.cc',
        'app/webrtc/webrtcsession_unittest.cc',
      ],
    },  # target libjingle_peerconnection_unittest
  ],
  'conditions': [
    ['OS=="linux"', {
      'targets': [
        {
          'target_name': 'libjingle_peerconnection_test_jar',
          'type': 'none',
          'actions': [
            {
              'variables': {
                'java_src_dir': 'app/webrtc/javatests/src',
                'java_files': [
                  'app/webrtc/javatests/src/org/webrtc/PeerConnectionTest.java',
                ],
              },
              'action_name': 'create_jar',
              'inputs': [
                'build/build_jar.sh',
                '<@(java_files)',
                '<(PRODUCT_DIR)/libjingle_peerconnection.jar',
                '<(DEPTH)/third_party/junit/junit-4.11.jar',
              ],
              'outputs': [
                '<(PRODUCT_DIR)/libjingle_peerconnection_test.jar',
              ],
              'action': [
                'build/build_jar.sh', '<(java_home)', '<@(_outputs)',
                '<(INTERMEDIATE_DIR)',
                '<(java_src_dir):<(PRODUCT_DIR)/libjingle_peerconnection.jar:<(DEPTH)/third_party/junit/junit-4.11.jar',
                '<@(java_files)'
              ],
            },
          ],
        },
        {
          'target_name': 'libjingle_peerconnection_java_unittest',
          'type': 'none',
          'actions': [
            {
              'action_name': 'copy libjingle_peerconnection_java_unittest',
              'inputs': [
                'app/webrtc/javatests/libjingle_peerconnection_java_unittest.sh',
                '<(PRODUCT_DIR)/libjingle_peerconnection_test_jar',
                '<(DEPTH)/third_party/junit/junit-4.11.jar',
              ],
              'outputs': [
                '<(PRODUCT_DIR)/libjingle_peerconnection_java_unittest',
              ],
              'action': [
                'bash', '-c',
                'rm -f <(PRODUCT_DIR)/libjingle_peerconnection_java_unittest && '
                'sed -e "s@GYP_JAVA_HOME@<(java_home)@" '
                '< app/webrtc/javatests/libjingle_peerconnection_java_unittest.sh '
                '> <(PRODUCT_DIR)/libjingle_peerconnection_java_unittest && '
                'cp <(DEPTH)/third_party/junit/junit-4.11.jar <(PRODUCT_DIR) && '
                'chmod u+x <(PRODUCT_DIR)/libjingle_peerconnection_java_unittest'
              ],
            },
          ],
        },
      ],
    }],
    ['libjingle_objc == 1', {
      'targets': [
        {
          'variables': {
            'infoplist_file': './app/webrtc/objctests/Info.plist',
          },
          'target_name': 'libjingle_peerconnection_objc_test',
          'type': 'executable',
          'mac_bundle': 1,
          'mac_bundle_resources': [
            '<(infoplist_file)',
          ],
          # The plist is listed above so that it appears in XCode's file list,
          # but we don't actually want to bundle it.
          'mac_bundle_resources!': [
            '<(infoplist_file)',
          ],
          'xcode_settings': {
            'CLANG_ENABLE_OBJC_ARC': 'YES',
            'INFOPLIST_FILE': '<(infoplist_file)',
          },
          'dependencies': [
            'gunit',
            'libjingle.gyp:libjingle_peerconnection_objc',
          ],
          'FRAMEWORK_SEARCH_PATHS': [
            '$(inherited)',
            '$(SDKROOT)/Developer/Library/Frameworks',
            '$(DEVELOPER_LIBRARY_DIR)/Frameworks',
          ],
          'sources': [
            'app/webrtc/objctests/RTCPeerConnectionSyncObserver.h',
            'app/webrtc/objctests/RTCPeerConnectionSyncObserver.m',
            'app/webrtc/objctests/RTCPeerConnectionTest.mm',
            'app/webrtc/objctests/RTCSessionDescriptionSyncObserver.h',
            'app/webrtc/objctests/RTCSessionDescriptionSyncObserver.m',
          ],
          'conditions': [
            ['OS=="mac" or OS=="ios"', {
              'sources': [
                # TODO(fischman): figure out if this works for ios or if it
                # needs a GUI driver.
                'app/webrtc/objctests/mac/main.mm',
              ],
            }],
          ],
        },
      ],
    }],
  ],
}
