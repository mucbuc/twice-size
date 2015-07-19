#!/usr/bin/env node

var assert = require( 'assert' )
  , events = require( 'events' )
  , cp = require( 'child_process' )
  , emitter = new events.EventEmitter()
  , Reader = require( './Reader' )
  , program = require( 'commander' )
  , join = require( 'path' ).join; 

program
	.version( '0.0.0' )
	.option( '-p, --prefix [path]', 'output path' )
	.parse( process.argv )

installDependencies( Reader.readDependencies() );

function installDependencies( dependencies, index ) {
	
	if (typeof index === 'undefined')
		index = 0;

	if (index < dependencies.length)
	{
		var dependency = dependencies[ index ]
	      , name = Reader.libName( dependency )
	      , child = cp.spawn( 'git', [ 
				'clone',
				'--depth=1',
				dependency,
				name
			], {
				stdio: 'inherit'
			} );

		emitter.once( 'next dependency', function() {
			installDependencies( dependencies, index + 1 );
		} ); 

		child.on( 'exit', function( code ) {
			if (!code) {
				console.log( 'repo cloned: ', name );
			}
			else { 
				console.log( 'repo clone failed: ', name );
			}
			emitter.emit( 'next dependency', dependency, name );
		});
	}
}
	
