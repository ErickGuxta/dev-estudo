// O que é uma Promise?
// Uma Promise é um objeto que representa o resultado eventual de uma operação assíncrona. Pode estar em um dos seguintes estados:

// Pending (pendente): A operação ainda está em andamento.
// Fulfilled (realizada): A operação foi concluída com sucesso e a promessa foi "resolvida" (com resolve).
// Rejected (rejeitada): A operação falhou e a promessa foi "rejeitada" (com reject).


const loginUserPromise = (email, password) => {
    return new Promise((resolve, reject) => {
        const error = false; // Simula se há um erro ou não
        if (error) {
            reject(new Error("Erro no login"));
        }
        console.log("User logged!");
        resolve({ email });
    });
};

const getUserVideos = (email) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(["video1", "video2", "video3"]); // Retorna uma lista de vídeos
        }, 2000);
    });
};

const getVideoDetails = (video) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ title: `${video} title` }); // Retorna detalhes de um vídeo
        }, 2500);
    });
};

// Encadeamento das Promises
loginUserPromise("felipe@gmail.com", "1234567")
    .then((user) => {
        // Passa o email para buscar os vídeos
        return getUserVideos(user.email); // Retorna a Promise de vídeos
    })
    .then((videos) => {
        console.log("Videos do usuário:", videos);
        // Passa o primeiro vídeo para obter detalhes
        return getVideoDetails(videos[0]); // Retorna a Promise com os detalhes
    })
    .then((videoDetails) => {
        console.log("Detalhes do vídeo:", videoDetails);
    })
    .catch((error) => {
        console.error("Erro:", error.message); // Trata erros em qualquer etapa
    });


// Promise.all
const yt = new Promise((resolve) => {
    setTimeout(() => {
      resolve("videos from youtube");
    }, 2000);
  });
  
  const fb = new Promise((resolve) => {
    setTimeout(() => {
      resolve("posts from facebook");
    }, 5000);
  });
  
  Promise.all([yt, fb]).then((result) => {
    console.log({ result });
  });