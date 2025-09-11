const arr = ['Vedant','Sarvesh', 'Ranade']

 function time (t1,t2){
    console.log('Time taken in ms :'+ (t2-t1))
 }

function my_name (array) {
    let t0 = performance.now()
    for(let i = 0; i<array.length; i++ ){
        if (array[i] ==='Ranade'){
            console.log('Found')
        }
    }
    let t1 = performance.now()
    time(t0,t1)
}

my_name(arr)