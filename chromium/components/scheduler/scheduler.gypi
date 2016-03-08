# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'scheduler_common_sources': [
      'common/scheduler_switches.cc',
      'common/scheduler_switches.h',
    ],
    'scheduler_sources': [
      'base/cancelable_closure_holder.cc',
      'base/cancelable_closure_holder.h',
      'base/lazy_now.cc',
      'base/lazy_now.h',
      'base/real_time_domain.cc',
      'base/real_time_domain.h',
      'base/task_queue.cc',
      'base/task_queue.h',
      'base/task_queue_impl.cc',
      'base/task_queue_impl.h',
      'base/task_queue_manager.cc',
      'base/task_queue_manager.h',
      'base/task_queue_manager_delegate.h',
      'base/task_queue_selector.cc',
      'base/task_queue_selector.h',
      'base/time_domain.cc',
      'base/time_domain.h',
      'base/work_queue.cc',
      'base/work_queue.h',
      'base/work_queue_sets.cc',
      'base/work_queue_sets.h',
      'base/pollable_thread_safe_flag.cc',
      'base/pollable_thread_safe_flag.h',
      'base/virtual_time_domain.cc',
      'base/virtual_time_domain.h',
      'base/enqueue_order.h',
      'base/enqueue_order.cc',
      'child/child_scheduler.h',
      'child/compositor_worker_scheduler.cc',
      'child/compositor_worker_scheduler.h',
      'child/idle_helper.cc',
      'child/idle_helper.h',
      'child/scheduler_helper.cc',
      'child/scheduler_helper.h',
      'child/scheduler_tqm_delegate.h',
      'child/scheduler_tqm_delegate_impl.cc',
      'child/scheduler_tqm_delegate_impl.h',
      'child/single_thread_idle_task_runner.cc',
      'child/single_thread_idle_task_runner.h',
      'child/virtual_time_tqm_delegate.cc',
      'child/virtual_time_tqm_delegate.h',
      'child/web_scheduler_impl.cc',
      'child/web_scheduler_impl.h',
      'child/web_task_runner_impl.cc',
      'child/web_task_runner_impl.h',
      'child/webthread_base.cc',
      'child/webthread_base.h',
      'child/webthread_impl_for_worker_scheduler.cc',
      'child/webthread_impl_for_worker_scheduler.h',
      'child/worker_scheduler.cc',
      'child/worker_scheduler.h',
      'child/worker_scheduler_impl.cc',
      'child/worker_scheduler_impl.h',
      'renderer/deadline_task_runner.cc',
      'renderer/deadline_task_runner.h',
      'renderer/idle_time_estimator.cc',
      'renderer/idle_time_estimator.h',
      'renderer/renderer_scheduler.cc',
      'renderer/renderer_scheduler.h',
      'renderer/renderer_scheduler_impl.cc',
      'renderer/renderer_scheduler_impl.h',
      'renderer/renderer_web_scheduler_impl.cc',
      'renderer/renderer_web_scheduler_impl.h',
      'renderer/render_widget_scheduling_state.cc',
      'renderer/render_widget_scheduling_state.h',
      'renderer/render_widget_signals.cc',
      'renderer/render_widget_signals.h',
      'renderer/task_cost_estimator.cc',
      'renderer/task_cost_estimator.h',
      'renderer/throttled_time_domain.cc',
      'renderer/throttled_time_domain.h',
      'renderer/throttling_helper.cc',
      'renderer/throttling_helper.h',
      'renderer/web_frame_scheduler_impl.cc',
      'renderer/web_frame_scheduler_impl.h',
      'renderer/web_view_scheduler_impl.cc',
      'renderer/web_view_scheduler_impl.h',
      'renderer/user_model.cc',
      'renderer/user_model.h',
      'renderer/webthread_impl_for_renderer_scheduler.cc',
      'renderer/webthread_impl_for_renderer_scheduler.h',
      'scheduler_export.h',
    ],
    'scheduler_test_support_sources': [
      'test/lazy_scheduler_message_loop_delegate_for_tests.cc',
      'test/lazy_scheduler_message_loop_delegate_for_tests.h',
    ],
  },
}
