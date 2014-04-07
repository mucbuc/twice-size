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
					'OS=="mac"', {
						'xcode_settings': {
		        			'OTHER_CFLAGS': [
		          				'-std=c++11', '-stdlib=libc++'
		        			],
		        		}
					}, {
						'cflags': [
							'-std=c++11', '-stdlib=libc++'
						]
					}		
				]
			]
        }
	]
}