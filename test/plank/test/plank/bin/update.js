#!/usr/bin/env node

var assert = require( 'assert' )
  , cp = require( 'child_process' )
  , Reader = require( './Reader' )
  , join = require( 'path' ).join;

function update( dependencies, index ) {
	if (typeof index === 'undefined') {
		index = 0;
	}

	if (index < dependencies.length) {
		var name = Reader.libName( dependencies[index] );
		console.log( 'pull ' + name );
		cp.exec( 
			'git -C '
			+ join( Reader.readOutputDir(), name )
			+ ' pull --squash origin master', 
			function(error, stdout, stderr) {
				if (error) throw error;
				console.log( stdout );
				update( dependencies, index + 1 );
			} ); 
	}
}

update( Reader.readDependencies() ); 
