CREATE TABLE alimento (
 id_alimento CHAR(10) NOT NULL,
 nombre CHAR(10),
 tipo CHAR(10),
 calorias CHAR(10)
);

ALTER TABLE alimento ADD CONSTRAINT PK_alimento PRIMARY KEY (id_alimento);


CREATE TABLE catalogoRoles (
 id_rol CHAR(10) NOT NULL,
 nombre CHAR(10)
);

ALTER TABLE catalogoRoles ADD CONSTRAINT PK_catalogoRoles PRIMARY KEY (id_rol);


CREATE TABLE ejercicio (
 id_ejercicio CHAR(10) NOT NULL,
 nombre CHAR(10),
 tipo CHAR(10),
 sets CHAR(10),
 repeticiones CHAR(10)
);

ALTER TABLE ejercicio ADD CONSTRAINT PK_ejercicio PRIMARY KEY (id_ejercicio);


CREATE TABLE usuario (
 id_usuario CHAR(10) NOT NULL,
 nombre CHAR(10),
 ap_paterno CHAR(10),
 ap_materno CHAR(10),
 email CHAR(10),
 contrasena CHAR(10),
 rol CHAR(10),
 id_rol CHAR(10) NOT NULL
);

ALTER TABLE usuario ADD CONSTRAINT PK_usuario PRIMARY KEY (id_usuario);


CREATE TABLE asesor (
 id_asesor CHAR(10) NOT NULL,
 id_usuario CHAR(10) NOT NULL,
 especialidad CHAR(10),
 experiencia CHAR(10)
);

ALTER TABLE asesor ADD CONSTRAINT PK_asesor PRIMARY KEY (id_asesor);


CREATE TABLE planAlimenticio (
 id_plan CHAR(10) NOT NULL,
 id_asesor CHAR(10) NOT NULL,
 descripcion CHAR(10)
);

ALTER TABLE planAlimenticio ADD CONSTRAINT PK_planAlimenticio PRIMARY KEY (id_plan);


CREATE TABLE rutina (
 id_rutina CHAR(10) NOT NULL,
 id_asesor CHAR(10) NOT NULL,
 descripcion CHAR(10)
);

ALTER TABLE rutina ADD CONSTRAINT PK_rutina PRIMARY KEY (id_rutina);


CREATE TABLE alimento_plan (
 id_alimento CHAR(10) NOT NULL,
 id_plan CHAR(10) NOT NULL
);

ALTER TABLE alimento_plan ADD CONSTRAINT PK_alimento_plan PRIMARY KEY (id_alimento,id_plan);


CREATE TABLE cliente (
 id_cliente CHAR(10) NOT NULL,
 id_usuario CHAR(10) NOT NULL,
 id_asesor CHAR(10),
 id_plan CHAR(10) NOT NULL,
 id_rutina CHAR(10) NOT NULL,
 objetivo CHAR(10),
 fecha_inicio CHAR(10)
);

ALTER TABLE cliente ADD CONSTRAINT PK_cliente PRIMARY KEY (id_cliente);


CREATE TABLE datosCorporales (
 id_datos CHAR(10) NOT NULL,
 id_asesor CHAR(10) NOT NULL,
 id_cliente CHAR(10) NOT NULL,
 peso CHAR(10),
 altura CHAR(10),
 imc CHAR(10),
 fecha CHAR(10)
);

ALTER TABLE datosCorporales ADD CONSTRAINT PK_datosCorporales PRIMARY KEY (id_datos);


CREATE TABLE ejercicio_rutina (
 id_ejercicio CHAR(10) NOT NULL,
 id_rutina CHAR(10) NOT NULL
);

ALTER TABLE ejercicio_rutina ADD CONSTRAINT PK_ejercicio_rutina PRIMARY KEY (id_ejercicio,id_rutina);


CREATE TABLE registroAlimenticio (
 id_registro CHAR(10) NOT NULL,
 id_cliente CHAR(10) NOT NULL,
 id_alimento CHAR(10),
 fecha CHAR(10),
 cantidad CHAR(10)
);

ALTER TABLE registroAlimenticio ADD CONSTRAINT PK_registroAlimenticio PRIMARY KEY (id_registro);


CREATE TABLE registroEjercicio (
 id_registro CHAR(10) NOT NULL,
 id_cliente CHAR(10) NOT NULL,
 id_ejercicio CHAR(10) NOT NULL,
 fecha CHAR(10),
 sets CHAR(10),
 repeticiones CHAR(10)
);

ALTER TABLE registroEjercicio ADD CONSTRAINT PK_registroEjercicio PRIMARY KEY (id_registro);


CREATE TABLE reporteProgreso (
 id_reporte CHAR(10) NOT NULL,
 id_asesor CHAR(10) NOT NULL,
 id_cliente CHAR(10) NOT NULL,
 fecha CHAR(10),
 observaciones CHAR(10)
);

ALTER TABLE reporteProgreso ADD CONSTRAINT PK_reporteProgreso PRIMARY KEY (id_reporte);


CREATE TABLE valoresCorporalesObjetivo (
 id_valores CHAR(10) NOT NULL,
 id_asesor CHAR(10) NOT NULL,
 id_cliente CHAR(10) NOT NULL,
 peso_objetivo CHAR(10),
 imc_objetivo CHAR(10)
);

ALTER TABLE valoresCorporalesObjetivo ADD CONSTRAINT PK_valoresCorporalesObjetivo PRIMARY KEY (id_valores);


ALTER TABLE usuario ADD CONSTRAINT FK_usuario_0 FOREIGN KEY (id_rol) REFERENCES catalogoRoles (id_rol);


ALTER TABLE asesor ADD CONSTRAINT FK_asesor_0 FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario);


ALTER TABLE planAlimenticio ADD CONSTRAINT FK_planAlimenticio_0 FOREIGN KEY (id_asesor) REFERENCES asesor (id_asesor);


ALTER TABLE rutina ADD CONSTRAINT FK_rutina_0 FOREIGN KEY (id_asesor) REFERENCES asesor (id_asesor);


ALTER TABLE alimento_plan ADD CONSTRAINT FK_alimento_plan_0 FOREIGN KEY (id_alimento) REFERENCES alimento (id_alimento);
ALTER TABLE alimento_plan ADD CONSTRAINT FK_alimento_plan_1 FOREIGN KEY (id_plan) REFERENCES planAlimenticio (id_plan);


ALTER TABLE cliente ADD CONSTRAINT FK_cliente_0 FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario);
ALTER TABLE cliente ADD CONSTRAINT FK_cliente_1 FOREIGN KEY (id_asesor) REFERENCES asesor (id_asesor);
ALTER TABLE cliente ADD CONSTRAINT FK_cliente_2 FOREIGN KEY (id_plan) REFERENCES planAlimenticio (id_plan);
ALTER TABLE cliente ADD CONSTRAINT FK_cliente_3 FOREIGN KEY (id_rutina) REFERENCES rutina (id_rutina);


ALTER TABLE datosCorporales ADD CONSTRAINT FK_datosCorporales_0 FOREIGN KEY (id_asesor) REFERENCES asesor (id_asesor);
ALTER TABLE datosCorporales ADD CONSTRAINT FK_datosCorporales_1 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente);


ALTER TABLE ejercicio_rutina ADD CONSTRAINT FK_ejercicio_rutina_0 FOREIGN KEY (id_ejercicio) REFERENCES ejercicio (id_ejercicio);
ALTER TABLE ejercicio_rutina ADD CONSTRAINT FK_ejercicio_rutina_1 FOREIGN KEY (id_rutina) REFERENCES rutina (id_rutina);


ALTER TABLE registroAlimenticio ADD CONSTRAINT FK_registroAlimenticio_0 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente);
ALTER TABLE registroAlimenticio ADD CONSTRAINT FK_registroAlimenticio_1 FOREIGN KEY (id_alimento) REFERENCES alimento (id_alimento);


ALTER TABLE registroEjercicio ADD CONSTRAINT FK_registroEjercicio_0 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente);
ALTER TABLE registroEjercicio ADD CONSTRAINT FK_registroEjercicio_1 FOREIGN KEY (id_ejercicio) REFERENCES ejercicio (id_ejercicio);


ALTER TABLE reporteProgreso ADD CONSTRAINT FK_reporteProgreso_0 FOREIGN KEY (id_asesor) REFERENCES asesor (id_asesor);
ALTER TABLE reporteProgreso ADD CONSTRAINT FK_reporteProgreso_1 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente);


ALTER TABLE valoresCorporalesObjetivo ADD CONSTRAINT FK_valoresCorporalesObjetivo_0 FOREIGN KEY (id_asesor) REFERENCES asesor (id_asesor);
ALTER TABLE valoresCorporalesObjetivo ADD CONSTRAINT FK_valoresCorporalesObjetivo_1 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente);


