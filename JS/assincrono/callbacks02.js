////PROBLEMAS COM CALLBACK  (função dentro de função, começa ficar muito confuso)


const loginUser = (email, password, onSucess, onError) => {
    setTimeout(() => {

        const error = false
        if (error == true) {
            return onError(new Error('error in login'))
        }

        console.log('user logged!');
        onSucess( 
            {
                emailUsuario: email,
                passwordUsuario: password
            }
        ) 
    }, 2000);

    console.log('after setTimeout')
};

//acrescentando uma função para mostrar os videos do usuarios depois de logado

const getUserVideos = (email, callback) => {
    setTimeout(() => {
        callback(['video1', 'video2', 'video3'])
    }, 2000);
}

//acrescentando uma função para mostrar detalhes de videos

const getVideosDetails = (videos, callback) => {
    setTimeout(() => {
        callback({title: 'video title'})
    }, 2500);
}

const user = loginUser(
    'gustavocostacnn@gmial.com', 
    '123456', 

    //PERCEBA QUE A IDEIA AQUI É QUE O PARÂMETRO VIDEO ARMAZENA OS DADOS DA CALLBACK

    (user) => {
        getUserVideos(user.emailUsuario, (videos) => {
            console.log({videos})
            getVideosDetails(videos[0], (videoDetails) => {
                console.log({videoDetails})
            })   
        })
    }, // quando eu uso a estrutura () => {}, estou falando que essa função será usada em um momento mais tarde


    (error) => {
        console.log({error});
    }
);



    