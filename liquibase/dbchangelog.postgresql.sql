-- liquibase formatted sql

-- changeset luke:1622082652929-1
CREATE TABLE "public"."auth_group" ("id" INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "name" VARCHAR(150) NOT NULL, CONSTRAINT "auth_group_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-2
CREATE TABLE "public"."auth_group_permissions" ("id" BIGINT GENERATED BY DEFAULT AS IDENTITY NOT NULL, "group_id" INTEGER NOT NULL, "permission_id" INTEGER NOT NULL, CONSTRAINT "auth_group_permissions_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-3
CREATE TABLE "public"."auth_permission" ("id" INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "name" VARCHAR(255) NOT NULL, "content_type_id" INTEGER NOT NULL, "codename" VARCHAR(100) NOT NULL, CONSTRAINT "auth_permission_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-4
CREATE TABLE "public"."django_content_type" ("id" INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "app_label" VARCHAR(100) NOT NULL, "model" VARCHAR(100) NOT NULL, CONSTRAINT "django_content_type_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-5
CREATE TABLE "public"."auth_user_groups" ("id" BIGINT GENERATED BY DEFAULT AS IDENTITY NOT NULL, "user_id" INTEGER NOT NULL, "group_id" INTEGER NOT NULL, CONSTRAINT "auth_user_groups_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-6
CREATE TABLE "public"."auth_user" ("id" INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "password" VARCHAR(128) NOT NULL, "last_login" TIMESTAMP WITH TIME ZONE, "is_superuser" BOOLEAN NOT NULL, "username" VARCHAR(150) NOT NULL, "first_name" VARCHAR(150) NOT NULL, "last_name" VARCHAR(150) NOT NULL, "email" VARCHAR(254) NOT NULL, "is_staff" BOOLEAN NOT NULL, "is_active" BOOLEAN NOT NULL, "date_joined" TIMESTAMP WITH TIME ZONE NOT NULL, CONSTRAINT "auth_user_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-7
CREATE TABLE "public"."auth_user_user_permissions" ("id" BIGINT GENERATED BY DEFAULT AS IDENTITY NOT NULL, "user_id" INTEGER NOT NULL, "permission_id" INTEGER NOT NULL, CONSTRAINT "auth_user_user_permissions_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-8
CREATE TABLE "public"."django_admin_log" ("id" INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "action_time" TIMESTAMP WITH TIME ZONE NOT NULL, "object_id" TEXT, "object_repr" VARCHAR(200) NOT NULL, "action_flag" SMALLINT NOT NULL, "change_message" TEXT NOT NULL, "content_type_id" INTEGER, "user_id" INTEGER NOT NULL, CONSTRAINT "django_admin_log_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-9
CREATE TABLE "public"."django_migrations" ("id" BIGINT GENERATED BY DEFAULT AS IDENTITY NOT NULL, "app" VARCHAR(255) NOT NULL, "name" VARCHAR(255) NOT NULL, "applied" TIMESTAMP WITH TIME ZONE NOT NULL, CONSTRAINT "django_migrations_pkey" PRIMARY KEY ("id"));

-- changeset luke:1622082652929-10
CREATE TABLE "public"."django_session" ("session_key" VARCHAR(40) NOT NULL, "session_data" TEXT NOT NULL, "expire_date" TIMESTAMP WITH TIME ZONE NOT NULL, CONSTRAINT "django_session_pkey" PRIMARY KEY ("session_key"));

-- changeset luke:1622082652929-11
ALTER TABLE "public"."auth_group" ADD CONSTRAINT "auth_group_name_key" UNIQUE ("name");

-- changeset luke:1622082652929-12
ALTER TABLE "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-13
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "public"."auth_group_permissions"("group_id");

-- changeset luke:1622082652929-14
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-15
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id");

-- changeset luke:1622082652929-16
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "public"."auth_group_permissions"("permission_id");

-- changeset luke:1622082652929-17
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "public"."auth_permission"("content_type_id");

-- changeset luke:1622082652929-18
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename");

-- changeset luke:1622082652929-19
ALTER TABLE "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-20
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model");

-- changeset luke:1622082652929-21
CREATE INDEX "auth_user_groups_group_id_97559544" ON "public"."auth_user_groups"("group_id");

-- changeset luke:1622082652929-22
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "public"."auth_user_groups"("user_id");

-- changeset luke:1622082652929-23
ALTER TABLE "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id");

-- changeset luke:1622082652929-24
ALTER TABLE "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "public"."auth_user" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-25
ALTER TABLE "public"."auth_user" ADD CONSTRAINT "auth_user_username_key" UNIQUE ("username");

-- changeset luke:1622082652929-26
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "public"."auth_user" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-27
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "public"."auth_user_user_permissions"("permission_id");

-- changeset luke:1622082652929-28
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "public"."auth_user_user_permissions"("user_id");

-- changeset luke:1622082652929-29
ALTER TABLE "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id");

-- changeset luke:1622082652929-30
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "public"."django_admin_log"("content_type_id");

-- changeset luke:1622082652929-31
ALTER TABLE "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "public"."django_content_type" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-32
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "public"."django_admin_log"("user_id");

-- changeset luke:1622082652929-33
CREATE INDEX "django_session_expire_date_a5c62663" ON "public"."django_session"("expire_date");

-- changeset luke:1622082652929-34
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-35
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "public"."django_content_type" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- changeset luke:1622082652929-36
ALTER TABLE "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "public"."auth_user" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;
