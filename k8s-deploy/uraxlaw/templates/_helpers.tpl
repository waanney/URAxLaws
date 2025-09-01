{{/*
Application name
*/}}
{{- define "uraxlaw.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Full application name
*/}}
{{- define "uraxlaw.fullname" -}}
{{- default .Release.Name .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "uraxlaw.labels" -}}
app.kubernetes.io/name: {{ include "uraxlaw.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "uraxlaw.selectorLabels" -}}
app.kubernetes.io/name: {{ include "uraxlaw.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
.env file content
*/}}
{{- define "uraxlaw.envContent" -}}
{{- $first := true -}}
{{- range $key, $val := .Values.env -}}
{{- if not $first -}}{{- "\n" -}}{{- end -}}
{{- $first = false -}}
{{ $key }}={{ $val }}
{{- end -}}
{{- end -}}
