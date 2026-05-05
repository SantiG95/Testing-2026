# Etapa 1: Construcción
FROM eclipse-temurin:21-jdk AS build
COPY . /app
WORKDIR /app
RUN ./mvnw clean package -DskipTests

# Etapa 2: Ejecución
FROM eclipse-temurin:21-jre
COPY --from=build /app/target/e-commerce3-0.0.1-SNAPSHOT.jar /app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]