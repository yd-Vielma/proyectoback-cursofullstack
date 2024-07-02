-- Creando la base de datos
CREATE DATABASE Restaurante;

-- Usando la base de datos
USE Restaurante;

-- Creando la primera Tabla comentarios
CREATE TABLE comentarios(
	ID_comentario INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Correo_electronico VARCHAR(100),
    Comentario VARCHAR(100),
    PRIMARY KEY (ID_Comentario)
);

-- creando la segunda tabla
CREATE TABLE valoracion(
	ID_valoracion INT NOT NULL AUTO_INCREMENT,
    usuario_number INT,
	platillo_number INT,
    puntos varchar(10),
    PRIMARY KEY (ID_valoracion),
    FOREIGN KEY (platillo_number) REFERENCES platillo(platillo_ID),
    FOREIGN KEY (usuario_number) REFERENCES comentarios(ID_comentario)
);

-- creacion de la ultima tabla
CREATE TABLE platillo(
	platillo_ID INT NOT NULL AUTO_INCREMENT,
    imagen_id int(2),
	plato VARCHAR(50),
    descripcion VARCHAR(150),
    precio INT(50),
    PRIMARY KEY (platillo_ID) 
);

CREATE TABLE imagen (
	Id_imagen INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(60),
    texto_alternativo VARCHAR (60),
    PRIMARY KEY (ID_imagen)
);    

-- Agregar valores a las tablas
INSERT INTO comentarios(nombre,Apellido,Correo_electronico, Comentario) VALUES
	('Yonathan','Diaz','yd@123gmail.com','El sitio es genial'),
    ('Lucas', 'Perez','lp@123hotmail.com','Comida sobrevalorada'),
    ('Emily','Watson','EmilyW@gmail.com','dolor de estomago'),
    ('Homer','Simpson','Hsimpsom@gmail.com','MMMMMMM Rosquillas ahhhhhg');
    

INSERT INTO imagen(url,texto_alternativo) VALUES
	('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/Mocktails-sin-alcohol.jpg','imagen coctail sin alcohol'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/Mousse-de-Frutas-del-Bosque.jpg','Mousee'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/Pappardelle.jpg','Pappardell'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/Roast-Beef-con-Pure.jpg','Roast-Beef'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/Smoothies-de-Frutas-Exotica.jpg','Smootie'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/Souffle-de-Mango-y-Coco.jpg','Soufflet'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/batatas-Rellenas.jpg','batatas'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/bizcocho-limon-glaseado.jpg','Biscocho de limon'),
    ('https://github.com/NoeliaMV/sitioresto.github.io/blob/master/ImgMenu/ceviche-de-lubina.jpg','Ceviche');
    

INSERT INTO platillo (imagen_id,plato,descripcion,precio) VALUES
	(1,'Cocktail sin alcohol', 'Nuestros Mocktails Creativos son la prueba de que la diversión no necesita ron ni vodka. Desde el Virgin Mojito con su frescura a base de menta y lima, hasta el intrigante Spritz sin Alcohol con su burbujeante Aperol sin vino. Cada sorbo es una celebración de la creatividad y el sabor. Así que, ¿por qué no brindar con algo diferente? ¡Salud!',35),
    (2,'Mousse de Frutas del Bosque', 'En un elegante vasito, servimos una mousse suave y aireada, coronada con frutos rojos frescos. Cada cucharada es un viaje a los bosques silvestres, donde los sabores naturales se mezclan en armonía. Ideal para aquellos que buscan un postre ligero y lleno de autenticidad. ¡Disfruta de la naturaleza en cada bocado!', 40),
    (3,'Pappardelle', 'El Pappardelle es más que un simple plato; es una obra maestra de la gastronomía italiana. Nuestra pasta Pappardelle es perfecta para absorber salsas espesas y sustanciosas. Servimos nuestro Pappardelle en platos amplios y elegantes, donde las cintas anchas se entrelazan, creando una presentación visualmente impactante. En nuestro restaurante, el Pappardelle es más que un plato. Es un viaje a la Italia más auténtica.', 25),
    (4,'Roast-Beef', 'En nuestro restaurante, servimos el Roast Beef con Puré de Papas en un plato de porcelana blanca. El roast beef se corta en rodajas generosas y se coloca sobre una cama de puré de papas. La salsa de carne se vierte con elegancia, y las verduras asadas se disponen alrededor del plato. El aroma a hierbas frescas y la textura suave del puré te invitarán a disfrutar cada bocado.',45);

INSERT INTO valoracion(usuario_number,platillo_number,puntos) VALUES
	(1,1,'2');



