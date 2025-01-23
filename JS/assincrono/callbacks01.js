//SIMULANDO LOGIN USER

//As funções onSucess e onError são funções callbacks
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

const user = loginUser(
    'gustavocostacnn@gmial.com', 
    '123456', 
    (user) => {
        console.log(`user: { email: '${user.emailUsuario}', password: '${user.passwordUsuario}' }`);
    }, // quando eu uso a estrutura () => {}, estou falando que essa função será usada em um momento mais tarde
    (error) => {
        console.log({error});
    }
);


//PROBLEMAS COM CALLBACK

    