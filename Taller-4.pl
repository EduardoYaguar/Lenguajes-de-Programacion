
materia('Matematicas', 3).
materia('Base de datos', 3).
materia('Analisis de algoritmos', 3).

estudiante('Juan', 'Matematicas').
estudiante('Juan', 'Base de datos').
estudiante('Andres', 'Base de datos').
estudiante('Anna', 'Analisis de algoritmos').


materiasxestudiante(Estudiante, Materia) :-
    estudiante(Estudiante, Materia).

estudiantesxmateria(Materia, Estudiante) :-
    estudiante(Estudiante, Materia).

creditosxestudiante(Estudiante, Creditos) :-
    estudiante(Estudiante, Materia),
    materia(Materia, Creditos).
