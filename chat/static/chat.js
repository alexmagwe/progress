var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', () => {
	let data={'data':'query_lessons'};
    socket.emit('request',data);
    $('form').submit(event => {
        event.preventDefault();
        let question = $('#question').val()
        socket.emit('request', 
	{'lesson': question
        })
        $('#question').val("").focus();

    })
})


socket.on('receive', (msg) => {
	if ( msg.lessons !==undefined && msg.lessons.length>1)
	{msg.lessons.forEach(display);
	}
	else if (typeof msg.lesson !== undefined ) {
display(msg);
    }}
)
const display=(data,index)=>{
    let container=$('#lesson-container')
        let lesson= document.createElement('div');
	let date=document.createElement('span')
		date.innerHTML=data.date
        lesson.innerHTML = data.lesson;
		lesson.append(date);
	lesson.className+='lesson';
	container.append(lesson);


}
