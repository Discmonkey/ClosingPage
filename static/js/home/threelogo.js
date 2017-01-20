var $nav = $('#navigation');
var scene = new THREE.Scene();
var height = $nav.height(),
	width = $nav.width();
var camera = new THREE.PerspectiveCamera(75, width/height,0.1,1000);
var renderer = new THREE.WebGLRenderer({alpha: true});
renderer.setSize(width, height);
$($nav).append( renderer.domElement );

var geometry = new THREE.BoxGeometry( 1, 1, 1 );

var ca = [0x4caf50, 0x4caf50, 0xFFA615, 0xFFA615,
0x12D8B1, 0x12D8B1, 0xFF7115,0xFF7115,
0x00ff37, 0x00ff37, 0xD4AFE5, 0xD4AFE5];

for (var i = 0; i<geometry.faces.length; i++) {
	geometry.faces[i].color.setHex(0x4caf50);
}
var material = new THREE.MeshPhongMaterial({ color: 0xffffff, vertexColors: THREE.FaceColors });
var cube = new THREE.Mesh( geometry, material );

camera.position.z = 1.7;
var directionalLight = new THREE.DirectionalLight( 0xffffff, 1  );
directionalLight.position.set( 0, 0, 1 );

scene.add(directionalLight);
scene.add(cube);


// var x_last = 0;
// var y_last = 0;
// var x_delta = 0;
// var y_delta = 0;
// $('canvas').mousemove(function(event){
// 	x_delta = .025 * (x_last - event.offsetX);
// 	y_delta = .025 * (y_last - event.offsetY);
// 	x_last = event.offsetX;
// 	y_last = event.offsetY;
// });

function render() {
    cube.rotation.y -= .01;
    cube.rotation.x -= .02;
    requestAnimationFrame(render);
    renderer.render( scene, camera );
}

render();

