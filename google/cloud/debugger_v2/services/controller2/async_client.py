# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.debugger_v2.types import controller
from google.cloud.debugger_v2.types import data
from .transports.base import Controller2Transport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import Controller2GrpcAsyncIOTransport
from .client import Controller2Client


class Controller2AsyncClient:
    """The Controller service provides the API for orchestrating a
    collection of debugger agents to perform debugging tasks. These
    agents are each attached to a process of an application which may
    include one or more replicas.

    The debugger agents register with the Controller to identify the
    application being debugged, the Debuggee. All agents that register
    with the same data, represent the same Debuggee, and are assigned
    the same ``debuggee_id``.

    The debugger agents call the Controller to retrieve the list of
    active Breakpoints. Agents with the same ``debuggee_id`` get the
    same breakpoints list. An agent that can fulfill the breakpoint
    request updates the Controller with the breakpoint result. The
    controller selects the first result received and discards the rest
    of the results. Agents that poll again for active breakpoints will
    no longer have the completed breakpoint in the list and should
    remove that breakpoint from their attached process.

    The Controller service does not provide a way to retrieve the
    results of a completed breakpoint. This functionality is available
    using the Debugger service.
    """

    _client: Controller2Client

    DEFAULT_ENDPOINT = Controller2Client.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = Controller2Client.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        Controller2Client.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        Controller2Client.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(Controller2Client.common_folder_path)
    parse_common_folder_path = staticmethod(Controller2Client.parse_common_folder_path)
    common_organization_path = staticmethod(Controller2Client.common_organization_path)
    parse_common_organization_path = staticmethod(
        Controller2Client.parse_common_organization_path
    )
    common_project_path = staticmethod(Controller2Client.common_project_path)
    parse_common_project_path = staticmethod(
        Controller2Client.parse_common_project_path
    )
    common_location_path = staticmethod(Controller2Client.common_location_path)
    parse_common_location_path = staticmethod(
        Controller2Client.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            Controller2AsyncClient: The constructed client.
        """
        return Controller2Client.from_service_account_info.__func__(Controller2AsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            Controller2AsyncClient: The constructed client.
        """
        return Controller2Client.from_service_account_file.__func__(Controller2AsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> Controller2Transport:
        """Returns the transport used by the client instance.

        Returns:
            Controller2Transport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(Controller2Client).get_transport_class, type(Controller2Client)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, Controller2Transport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the controller2 client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.Controller2Transport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = Controller2Client(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def register_debuggee(
        self,
        request: controller.RegisterDebuggeeRequest = None,
        *,
        debuggee: data.Debuggee = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> controller.RegisterDebuggeeResponse:
        r"""Registers the debuggee with the controller service.

        All agents attached to the same application must call this
        method with exactly the same request content to get back the
        same stable ``debuggee_id``. Agents should call this method
        again whenever ``google.rpc.Code.NOT_FOUND`` is returned from
        any controller method.

        This protocol allows the controller service to disable
        debuggees, recover from data loss, or change the ``debuggee_id``
        format. Agents must handle ``debuggee_id`` value changing upon
        re-registration.

        Args:
            request (:class:`google.cloud.debugger_v2.types.RegisterDebuggeeRequest`):
                The request object. Request to register a debuggee.
            debuggee (:class:`google.cloud.debugger_v2.types.Debuggee`):
                Required. Debuggee information to register. The fields
                ``project``, ``uniquifier``, ``description`` and
                ``agent_version`` of the debuggee must be set.

                This corresponds to the ``debuggee`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.RegisterDebuggeeResponse:
                Response for registering a debuggee.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = controller.RegisterDebuggeeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if debuggee is not None:
            request.debuggee = debuggee

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.register_debuggee,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_active_breakpoints(
        self,
        request: controller.ListActiveBreakpointsRequest = None,
        *,
        debuggee_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> controller.ListActiveBreakpointsResponse:
        r"""Returns the list of all active breakpoints for the debuggee.

        The breakpoint specification (``location``, ``condition``, and
        ``expressions`` fields) is semantically immutable, although the
        field values may change. For example, an agent may update the
        location line number to reflect the actual line where the
        breakpoint was set, but this doesn't change the breakpoint
        semantics.

        This means that an agent does not need to check if a breakpoint
        has changed when it encounters the same breakpoint on a
        successive call. Moreover, an agent should remember the
        breakpoints that are completed until the controller removes them
        from the active list to avoid setting those breakpoints again.

        Args:
            request (:class:`google.cloud.debugger_v2.types.ListActiveBreakpointsRequest`):
                The request object. Request to list active breakpoints.
            debuggee_id (:class:`str`):
                Required. Identifies the debuggee.
                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.ListActiveBreakpointsResponse:
                Response for listing active
                breakpoints.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = controller.ListActiveBreakpointsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if debuggee_id is not None:
            request.debuggee_id = debuggee_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_active_breakpoints,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_active_breakpoint(
        self,
        request: controller.UpdateActiveBreakpointRequest = None,
        *,
        debuggee_id: str = None,
        breakpoint_: data.Breakpoint = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> controller.UpdateActiveBreakpointResponse:
        r"""Updates the breakpoint state or mutable fields. The entire
        Breakpoint message must be sent back to the controller service.

        Updates to active breakpoint fields are only allowed if the new
        value does not change the breakpoint specification. Updates to
        the ``location``, ``condition`` and ``expressions`` fields
        should not alter the breakpoint semantics. These may only make
        changes such as canonicalizing a value or snapping the location
        to the correct line of code.

        Args:
            request (:class:`google.cloud.debugger_v2.types.UpdateActiveBreakpointRequest`):
                The request object. Request to update an active
                breakpoint.
            debuggee_id (:class:`str`):
                Required. Identifies the debuggee
                being debugged.

                This corresponds to the ``debuggee_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            breakpoint_ (:class:`google.cloud.debugger_v2.types.Breakpoint`):
                Required. Updated breakpoint information. The field
                ``id`` must be set. The agent must echo all Breakpoint
                specification fields in the update.

                This corresponds to the ``breakpoint_`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.debugger_v2.types.UpdateActiveBreakpointResponse:
                Response for updating an active
                breakpoint. The message is defined to
                allow future extensions.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([debuggee_id, breakpoint_])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = controller.UpdateActiveBreakpointRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if debuggee_id is not None:
            request.debuggee_id = debuggee_id
        if breakpoint_ is not None:
            request.breakpoint_ = breakpoint_

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_active_breakpoint,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-debugger-client",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("Controller2AsyncClient",)
