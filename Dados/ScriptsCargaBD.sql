-- Escolaridade
INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Educação infantil','Oferece orientações básicas para crianças mais jovens (até os 5 anos de idade, normalmente)',1,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Ensino fundamental','Compreende um período de nove anos e é obrigatório para crianças com idade a partir dos seis anos.',2,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Ensino médio','Oferece formação voltada para o mercado de trabalho, o aprimoramento do cidadão como pessoa humana e o aprofundamento dos conhecimentos adquiridos nas etapas anteriores.',3,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Ensino superior','Ministrado nas instituições de ensino superior, sejam elas públicas ou privadas, com formações específicas em diversas áreas do conhecimento profissional e científico.',4,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Ensino superior','Fornece base ampla de conhecimento em uma área de estudo escolhida, além de desenvolver habilidades gerais e específicas do campo de estudo para atuação profissional.',5,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Pós-graduação','Programa acadêmico oferecido após a conclusão da graduação, focado em campo específico de estudo e destinado a aprofundar o conhecimento e desenvolver habilidades especializadas.',6,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Mestrado','Programa acadêmico de pós-graduação focado em um campo específico, proporcionando conhecimento avançado e habilidades de pesquisa.',7,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Doutorado','Mais alto nível de estudo acadêmico, envolvendo pesquisa original e contribuições significativas para um campo específico, resultando na concessão de um título de doutor.',8,'2024-05-01',0);

INSERT INTO jogadores_escolaridade (nm_escolaridade,ds_escolaridade,vl_escolaridade,dt_inclusao,id_usuario_inclusao) 
VALUES ('Não Estuda','Não frequenta escola',0,'2024-05-01',0);


-- Idioma
INSERT INTO jogadores_idioma (nm_idioma,ds_idioma,nm_arquivo_imagem,nm_arquivo_estilo_css,dt_inclusao,id_usuario_inclusao)
VALUES ('Português','Idioma falado atualmente no Brasil.','','','2024-05-01',0);
  
INSERT INTO jogadores_idioma (nm_idioma,ds_idioma,nm_arquivo_imagem,nm_arquivo_estilo_css,dt_inclusao,id_usuario_inclusao)
VALUES ('Tupi','Idioma ancestral brasileiro em pratica por alguns grupos isolados.','','','2024-05-01',0);  


-- Nível Jogador
INSERT INTO jogos_nivel_jogador (nm_nivel_jogador,ds_nivel_jogador,vl_nivel_jogador,dt_inclusao,id_usuario_inclusao)
VALUES ('Iniciante','Nível inicial',,'2024-05-01',0);

INSERT INTO jogos_nivel_jogador (nm_nivel_jogador,ds_nivel_jogador,vl_nivel_jogador,dt_inclusao,id_usuario_inclusao)
VALUES ('Intermediário','Nível intermediário',2,'2024-05-01',0);

INSERT INTO jogos_nivel_jogador (nm_nivel_jogador,ds_nivel_jogador,vl_nivel_jogador,dt_inclusao,id_usuario_inclusao)
VALUES ('Avançado','Nível avançado',3,'2024-05-01',0);

- Nível Dificuldade dos jogos_nivel_jogadorINSERT INTO jogos_nivel_dificuldade (nm_nivel_dificuldade,ds_nivel_dificuldade,vl_nivel_dificuldade,dt_inclusao,id_usuario_inclusao)
VALUES ('Super-fácil','Nível super-fácil',1,'2024-05-01',0);

INSERT INTO jogos_nivel_dificuldade (nm_nivel_dificuldade,ds_nivel_dificuldade,vl_nivel_dificuldade,dt_inclusao,id_usuario_inclusao)
VALUES ('Fácil','Nível fácil',2,'2024-05-01',0);

INSERT INTO jogos_nivel_dificuldade (nm_nivel_dificuldade,ds_nivel_dificuldade,vl_nivel_dificuldade,dt_inclusao,id_usuario_inclusao)
VALUES ('Médio','Nível médio',3,'2024-05-01',0);

INSERT INTO jogos_nivel_dificuldade (nm_nivel_dificuldade,ds_nivel_dificuldade,vl_nivel_dificuldade,dt_inclusao,id_usuario_inclusao)
VALUES ('Difícil','Nível difícil',4,'2024-05-01',0);

INSERT INTO jogos_nivel_dificuldade (nm_nivel_dificuldade,ds_nivel_dificuldade,vl_nivel_dificuldade,dt_inclusao,id_usuario_inclusao)
VALUES ('Super-Difícil','Nível super difícil',5,'2024-05-01',0);

-- Jogos
INSERT INTO jogos_jogo (nm_jogo,ds_jogo,t_inclusao,id_usuario_inclusao)
VALUES ('QUIZ','Jogo de perguntas em um idioma e com opções de respostas em outro','2024-05-01',0);

INSERT INTO jogos_jogo (nm_jogo,ds_jogo,dt_inclusao,id_usuario_inclusao)
VALUES ('Jogo da memória','Jogo para teste da memória atráves de imagens','2024-05-01',0);
  
INSERT INTO jogos_jogo (nm_jogo,ds_jogo,dt_inclusao,id_usuario_inclusao)
VALUES ('Palavras Cruzadas','Jogo para, mediante dicas, combinação de palavras vertical e horizontalmente','2024-05-01',0);
  

-- Jogador
INSERT INTO jogadores_jogador (nm_jogador,nm_avatar,nm_arquivo_imagem,dt_nascimento,cd_cep,nm_email,nm_senha,dt_inclusao,id_usuario_inclusao,id_idioma_id,id_escolaridade_id,tp_genero)
VALUES ('Teste da Silva','TESTE','','2000-12-01','04512100','teste@gmail.com','teste','2024-05-01',0,1,3,'M');


