{
	'targets': [
		{
			'target_name': 'test', 
			'type': 'executable',
			'sources': [
				'src/main.cpp'
			],
			'includes':[
				'../twice-size.gypi'
			],
			'include_dirs': [
				'../'
			],
			'conditions': [
				[
					'OS=="ios"', {
						'xcode_settings': {
							'TARGETED_DEVICE_FAMILY': '1,2',
							'CODE_SIGN_IDENTITY': 'iPhone Developer',
							'IPHONEOS_DEPLOYMENT_TARGET': '5.0',
							'ARCHS': '$(ARCHS_STANDARD_32_64_BIT)',
						}
					}, {
						'cflags': [
							'-std=c++11', '-stdlib=libc++'
						]
					}		
				]
			]
        }
	],
	'conditions': [
		[
			'OS=="ios"', {
				'xcode_settings': {
					'SDKROOT': 'iphoneos',
				} # xcode_settings
			} ],
		] 


}