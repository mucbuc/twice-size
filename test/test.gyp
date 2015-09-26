{
	'includes':[
		'lib/twice-size/twice-size.gypi',
	],#inclues
	'target_defaults': {
		'target_name': 'test',
		'type': 'executable',
		'sources': [
			'src/main.cpp',
			'src/tests.h'
		], #sources
		'include_dirs': [
			'.'
		], #include_dirs		
	}, #target_defaults
}