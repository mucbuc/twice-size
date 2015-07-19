{
	'includes':[
		'lib/twice-size/twice-size.gypi',
		'plank/def/cpp11-gcc.gypi',
		'plank/def/mac-targets.gypi',
		'plank/def/plank.gypi',
	],#inclues
	'target_defaults': {
		'target_name': 'test',
		'type': 'executable',
		'sources': [
			'src/main.cpp',
			'src/tests.h'
		], #sources
		'include_dirs': [
			'plank/src/',
			'.'
		], #include_dirs		
	}, #target_defaults
}